"""Attachment discovery, resolution, and copying for Apple Notes."""

import mimetypes
import re
import shutil
from pathlib import Path

from bs4 import BeautifulSoup

from . import applescript
from .models import Attachment

MEDIA_DIR = Path.home() / "Library/Group Containers/group.com.apple.notes/Media"


def _classify_media_type(filename: str) -> str:
    """Classify a file as image, pdf, or other based on extension."""
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


def _build_media_index() -> dict[str, Path]:
    """Scan the Apple Notes Media directory and index files by name."""
    index: dict[str, Path] = {}
    if not MEDIA_DIR.exists():
        return index
    for path in MEDIA_DIR.rglob("*"):
        if path.is_file():
            index[path.name] = path
    return index


def _find_attachment_on_disk(
    attachment_name: str, media_index: dict[str, Path]
) -> Path | None:
    """Try to locate an attachment file in the Media directory."""
    # Direct name match
    if attachment_name in media_index:
        return media_index[attachment_name]
    # Case-insensitive match
    lower_name = attachment_name.lower()
    for name, path in media_index.items():
        if name.lower() == lower_name:
            return path
    return None


def resolve_attachments(
    html_body: str, note_id: str, note_name: str
) -> list[Attachment]:
    """Discover and resolve attachments for a note.

    Uses two strategies:
    1. Parse HTML for <img> and <object> tags with file references
    2. Fall back to AppleScript attachment enumeration + Media dir scan
    """
    media_index = _build_media_index()
    attachments: list[Attachment] = []
    seen_filenames: set[str] = set()
    note_slug = _sanitize_filename(note_name)[:50]

    # Strategy 1: Parse HTML for embedded media references
    soup = BeautifulSoup(html_body, "html.parser")

    for img in soup.find_all("img"):
        src = img.get("src", "")
        if not src:
            continue
        # Extract filename from src (could be file:// URL or path)
        src_path = Path(src.replace("file://", ""))
        original_name = src_path.name

        # Try to find on disk
        disk_path = _find_attachment_on_disk(original_name, media_index)
        if disk_path is None:
            # Try the full path directly
            if src_path.exists():
                disk_path = src_path

        if disk_path and disk_path.name not in seen_filenames:
            safe_name = f"{note_slug}_{_sanitize_filename(disk_path.name)}"
            attachments.append(Attachment(
                original_path=disk_path,
                filename=safe_name,
                media_type=_classify_media_type(disk_path.name),
                note_id=note_id,
            ))
            seen_filenames.add(disk_path.name)

    for obj in soup.find_all("object"):
        data = obj.get("data", "")
        if not data:
            continue
        data_path = Path(data.replace("file://", ""))
        original_name = data_path.name

        disk_path = _find_attachment_on_disk(original_name, media_index)
        if disk_path is None and data_path.exists():
            disk_path = data_path

        if disk_path and disk_path.name not in seen_filenames:
            safe_name = f"{note_slug}_{_sanitize_filename(disk_path.name)}"
            attachments.append(Attachment(
                original_path=disk_path,
                filename=safe_name,
                media_type=_classify_media_type(disk_path.name),
                note_id=note_id,
            ))
            seen_filenames.add(disk_path.name)

    # Strategy 2: AppleScript fallback for attachments not found in HTML
    try:
        as_attachments = applescript.get_note_attachments(note_id)
    except (RuntimeError, TimeoutError):
        as_attachments = []

    for att_info in as_attachments:
        att_name = att_info["name"]
        if att_name in seen_filenames:
            continue

        disk_path = _find_attachment_on_disk(att_name, media_index)
        if disk_path:
            safe_name = f"{note_slug}_{_sanitize_filename(disk_path.name)}"
            attachments.append(Attachment(
                original_path=disk_path,
                filename=safe_name,
                media_type=_classify_media_type(disk_path.name),
                note_id=note_id,
            ))
            seen_filenames.add(disk_path.name)

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
