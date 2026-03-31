"""Output directory writer and ZIP packaging."""

import re
import zipfile
from pathlib import Path

from .attachments import copy_attachments
from .converter import convert_note
from .models import Note


def _sanitize_note_filename(name: str) -> str:
    """Create a safe filename from a note title."""
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    # Limit length
    if len(name) > 100:
        name = name[:100].rstrip()
    return name or "Untitled"


def _deduplicate_filename(filename: str, existing: set[str]) -> str:
    """Add folder suffix or counter if filename already exists."""
    if filename not in existing:
        return filename
    stem = Path(filename).stem
    suffix = Path(filename).suffix
    counter = 2
    while True:
        candidate = f"{stem} ({counter}){suffix}"
        if candidate not in existing:
            return candidate
        counter += 1


def write_export(
    notes: list[Note],
    output_dir: Path,
    create_zip: bool = True,
    on_warning: callable | None = None,
) -> tuple[Path, Path | None, list[str]]:
    """Write all notes and attachments to the output directory.

    Returns:
        Tuple of (output_dir, zip_path_or_None, list_of_warnings)
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = output_dir / "assets"
    warnings: list[str] = []
    used_filenames: set[str] = set()

    for note in notes:
        # Copy attachments first
        att_warnings = copy_attachments(note.attachments, assets_dir)
        warnings.extend(att_warnings)

        # Convert note to markdown
        markdown = convert_note(note)

        # Determine output filename
        base_name = _sanitize_note_filename(note.name)
        filename = f"{base_name}.md"

        # If duplicate, append folder name
        if filename in used_filenames:
            filename = f"{base_name} ({note.folder}).md"

        # Still duplicated? Add counter
        filename = _deduplicate_filename(filename, used_filenames)
        used_filenames.add(filename)

        # Write the markdown file
        note_path = output_dir / filename
        note_path.write_text(markdown, encoding="utf-8")

    # Create ZIP if requested
    zip_path = None
    if create_zip:
        zip_path = output_dir.parent / f"{output_dir.name}.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for file in sorted(output_dir.rglob("*")):
                if file.is_file():
                    arcname = file.relative_to(output_dir)
                    zf.write(file, arcname)

    return output_dir, zip_path, warnings
