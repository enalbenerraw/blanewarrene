"""Attachment discovery, resolution, and copying for Apple Notes.

Apple Notes does not expose attachment file references in the AppleScript
``body`` of a note, and ``name of attachment`` is unreliable (often
``missing value`` for pasted images, PDFs, and scanned documents). The only
robust path is to enumerate attachments via AppleScript, parse the Core Data
primary key out of each attachment id, then resolve the file through
``NoteStore.sqlite``:

    AppleScript id  ->  .../ICAttachment/p<Z_PK>
    ZICCLOUDSYNCINGOBJECT[Z_PK].ZMEDIA  ->  media row
    media row .ZIDENTIFIER  ->  Media/<uuid>/ directory
    media row .ZFILENAME    ->  real filename on disk

The media file then lives at
``Accounts/*/Media/<uuid>/<revision>/<filename>``.
"""

import atexit
import mimetypes
import re
import shutil
import sqlite3
import tempfile
from pathlib import Path
from typing import Callable

from .models import Attachment
from . import applescript

NOTES_CONTAINER = (
    Path.home() / "Library/Group Containers/group.com.apple.notes"
)
NOTESTORE_DB = NOTES_CONTAINER / "NoteStore.sqlite"
ACCOUNTS_DIR = NOTES_CONTAINER / "Accounts"

# UTIs whose extensions mimetypes can miss; map straight to our buckets.
_IMAGE_UTIS = {
    "public.jpeg", "public.png", "public.tiff", "public.heic",
    "public.heif", "com.compuserve.gif", "org.webmproject.webp",
    "com.apple.icns",
}
_PDF_UTIS = {"com.adobe.pdf"}

_ATT_PK_RE = re.compile(r"/p(\d+)\b")

_db_conn: sqlite3.Connection | None = None
_db_status: str | None = None
_db_status_reported: bool = False
_resolver_ready: bool | None = None


def _classify_media_type(filename: str, uti: str | None = None) -> str:
    """Classify a file as image, pdf, or other from its UTI or extension."""
    if uti:
        if uti in _IMAGE_UTIS or uti.startswith("public.") and "image" in uti:
            return "image"
        if uti in _PDF_UTIS:
            return "pdf"
    mime, _ = mimetypes.guess_type(filename)
    if mime:
        if mime.startswith("image/"):
            return "image"
        if mime == "application/pdf":
            return "pdf"
    return "other"


def _sanitize_filename(name: str) -> str:
    """Make a filename safe for the filesystem."""
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name or "unnamed"


def _open_notestore() -> sqlite3.Connection | None:
    """Open NoteStore.sqlite read-only without disturbing the live Notes app.

    Notes keeps the database open in WAL mode. A read-only connection
    coexists safely with that writer and sees current data. If the live open
    fails (locking, unreadable WAL), fall back to a temp-dir copy of the
    database and its sidecar files.

    Records a diagnostic status on failure so callers can surface an
    actionable warning instead of silently exporting zero attachments.
    """
    global _db_conn, _db_status
    if _db_conn is not None:
        return _db_conn

    if not NOTES_CONTAINER.exists():
        _db_status = (
            f"Apple Notes container not found at {NOTES_CONTAINER}. "
            "This tool requires the macOS Notes app with local data; "
            "iCloud-only accounts without local copies cannot be exported."
        )
        return None

    try:
        readable = NOTESTORE_DB.exists()
    except PermissionError as e:
        _db_status = (
            f"Permission denied reading {NOTESTORE_DB} ({e}). Grant Full "
            "Disk Access to the process running notes2notion: System "
            "Settings > Privacy & Security > Full Disk Access, then add "
            "your terminal app and Notes2NotionUX.app and relaunch it."
        )
        return None
    if not readable:
        _db_status = f"NoteStore.sqlite not found at {NOTESTORE_DB}."
        return None

    # Primary: read-only connection against the live database.
    try:
        conn = sqlite3.connect(
            f"file:{NOTESTORE_DB}?mode=ro", uri=True, timeout=5
        )
        conn.execute("SELECT 1 FROM ZICCLOUDSYNCINGOBJECT LIMIT 1")
        _db_conn = conn
        return _db_conn
    except (sqlite3.OperationalError, sqlite3.DatabaseError):
        pass

    # Fallback: copy the db plus WAL/SHM sidecars and open the copy.
    try:
        tmp = Path(tempfile.mkdtemp(prefix="n2n_notestore_"))
        atexit.register(shutil.rmtree, tmp, ignore_errors=True)
        for suffix in ("", "-wal", "-shm"):
            src = Path(str(NOTESTORE_DB) + suffix)
            if src.exists():
                shutil.copy2(src, tmp / src.name)
        conn = sqlite3.connect(
            f"file:{tmp / NOTESTORE_DB.name}?mode=ro", uri=True
        )
        conn.execute("SELECT 1 FROM ZICCLOUDSYNCINGOBJECT LIMIT 1")
        _db_conn = conn
        return _db_conn
    except (OSError, sqlite3.Error) as e:
        _db_status = (
            f"Could not open NoteStore.sqlite read-only ({e}). "
            "Attachments cannot be resolved."
        )
        return None


def get_resolver_status() -> str | None:
    """Return a one-time diagnostic message about the resolver, if any."""
    return _db_status


def _report_status(on_warning: Callable[[str], None] | None) -> None:
    """Emit the resolver status to on_warning at most once per process."""
    global _db_status_reported
    if _db_status_reported or on_warning is None:
        return
    if _db_status:
        on_warning(_db_status)
        _db_status_reported = True


def probe_notestore_access() -> tuple[bool, str | None]:
    """Check whether NoteStore.sqlite can be opened (Full Disk Access).

    Returns ``(ok, message)``; ``message`` is the actionable diagnostic
    when access is unavailable. Backs the CLI ``--check-access`` preflight
    so the GUI can warn before a user invests effort in an export that
    would silently drop every attachment.
    """
    if _open_notestore() is not None:
        return True, None
    return False, get_resolver_status()


def _parse_attachment_pk(coredata_id: str) -> int | None:
    """Extract the Core Data Z_PK from an AppleScript attachment id.

    e.g. ``x-coredata://<store>/ICAttachment/p178252`` -> ``178252``.
    """
    m = _ATT_PK_RE.search(coredata_id)
    return int(m.group(1)) if m else None


def _media_file_for_pk(
    conn: sqlite3.Connection, z_pk: int
) -> tuple[Path, str, str] | None:
    """Resolve an attachment Z_PK to (disk_path, original_name, media_type).

    Returns None when the attachment has no backing media file (URL
    previews, bookmarks, and other link-only attachments), which is an
    expected skip rather than a failure.
    """
    row = conn.execute(
        """
        SELECT m.ZIDENTIFIER, m.ZFILENAME, a.ZFILENAME, a.ZTYPEUTI
        FROM ZICCLOUDSYNCINGOBJECT a
        LEFT JOIN ZICCLOUDSYNCINGOBJECT m ON a.ZMEDIA = m.Z_PK
        WHERE a.Z_PK = ?
        """,
        (z_pk,),
    ).fetchone()
    if row is None:
        return None

    media_uuid, media_filename, att_filename, att_uti = row
    if not media_uuid:
        return None  # link-only attachment, no file to export

    original_name = media_filename or att_filename
    media_dir = next(ACCOUNTS_DIR.glob(f"*/Media/{media_uuid}"), None)
    if media_dir is None or not media_dir.is_dir():
        return None

    disk_path: Path | None = None
    if original_name:
        disk_path = next(media_dir.rglob(_sanitize_filename(original_name)), None)
    if disk_path is None:
        # Some media (drawings, scans) are stored under a UUID filename;
        # the sqlite filename is still the correct export name.
        disk_path = next((p for p in media_dir.rglob("*") if p.is_file()), None)
    if disk_path is None:
        return None

    name = original_name or disk_path.name
    return disk_path, name, _classify_media_type(name, att_uti)


def resolve_attachments(
    html_body: str,
    note_id: str,
    note_name: str,
    on_warning: Callable[[str], None] | None = None,
) -> list[Attachment]:
    """Discover and resolve a note's attachments via AppleScript + sqlite.

    ``html_body`` is accepted for signature compatibility but is not used:
    the scriptable note body never contains attachment file references.
    """
    conn = _open_notestore()
    _report_status(on_warning)
    if conn is None:
        return []

    try:
        as_attachments = applescript.get_note_attachments(note_id)
    except (RuntimeError, TimeoutError):
        as_attachments = []
    if not as_attachments:
        return []

    note_slug = _sanitize_filename(note_name)[:50]
    attachments: list[Attachment] = []
    seen: set[Path] = set()
    unresolved: list[str] = []

    for att in as_attachments:
        z_pk = _parse_attachment_pk(att["id"])
        if z_pk is None:
            unresolved.append(att.get("name") or att["id"])
            continue
        try:
            resolved = _media_file_for_pk(conn, z_pk)
        except sqlite3.Error:
            resolved = None
        if resolved is None:
            # No media row == link-only attachment: an expected skip.
            continue
        disk_path, original_name, media_type = resolved
        if disk_path in seen:
            continue
        seen.add(disk_path)
        safe_name = f"{note_slug}_{_sanitize_filename(original_name)}"
        attachments.append(Attachment(
            original_path=disk_path,
            filename=safe_name,
            media_type=media_type,
            note_id=note_id,
        ))

    if unresolved and on_warning:
        on_warning(
            f"'{note_name}': {len(unresolved)} attachment(s) had an "
            f"unparseable id and were skipped (sample: {unresolved[:3]})."
        )

    return attachments


def copy_attachments(
    attachments: list[Attachment], assets_dir: Path
) -> list[str]:
    """Copy attachment files to the output assets directory.

    Returns list of warnings for any files that couldn't be copied.
    """
    assets_dir.mkdir(parents=True, exist_ok=True)
    warnings: list[str] = []

    for att in attachments:
        dest = assets_dir / att.filename
        # Handle filename collisions
        if dest.exists():
            stem = dest.stem
            suffix = dest.suffix
            counter = 1
            while dest.exists():
                dest = assets_dir / f"{stem}_{counter}{suffix}"
                counter += 1
            att.filename = dest.name

        try:
            shutil.copy2(att.original_path, dest)
        except (OSError, FileNotFoundError) as e:
            warnings.append(f"Could not copy '{att.original_path.name}': {e}")

    return warnings
