"""Orchestrates extraction of notes and attachments from Apple Notes."""

from typing import Callable

from . import applescript
from .models import Attachment, ExportConfig, Folder, Note
from .attachments import resolve_attachments


def discover_folders() -> list[Folder]:
    """List all folders in Notes.app."""
    raw_folders = applescript.list_folders()
    return [
        Folder(name=f["name"], note_count=f["note_count"])
        for f in raw_folders
    ]


def extract_notes(
    config: ExportConfig,
    on_progress: Callable[[str, int, int], None] | None = None,
    on_warning: Callable[[str], None] | None = None,
) -> list[Note]:
    """Extract all notes matching the export config.

    Args:
        config: Export configuration specifying folders and output.
        on_progress: Callback(note_name, current, total) for progress updates.
        on_warning: Callback(message) for non-fatal warnings.

    Returns:
        List of extracted Note objects.
    """
    all_folders = discover_folders()

    if config.folders is not None:
        target_folders = [f for f in all_folders if f.name in config.folders]
    else:
        target_folders = all_folders

    # Count total notes for progress tracking
    total_notes = sum(f.note_count for f in target_folders)
    current = 0
    notes: list[Note] = []
    skipped: list[tuple[str, str, str]] = []

    for folder in target_folders:
        try:
            note_metas = applescript.list_notes_in_folder(folder.name)
        except (RuntimeError, TimeoutError) as e:
            if on_warning:
                on_warning(f"Skipped folder '{folder.name}': {e}")
            current += folder.note_count
            continue

        for meta in note_metas:
            current += 1
            note_name = meta["name"]

            if on_progress:
                on_progress(note_name, current, total_notes)

            try:
                html_body = applescript.get_note_body(meta["id"])
            except (RuntimeError, TimeoutError) as e:
                reason = str(e)
                skipped.append((note_name, folder.name, reason))
                if on_warning:
                    on_warning(
                        f"Skipped '{note_name}' in {folder.name}: {reason}"
                    )
                continue

            # Resolve attachments
            attachments: list[Attachment] = []
            try:
                attachments = resolve_attachments(
                    html_body, meta["id"], note_name
                )
            except Exception as e:
                if on_warning:
                    on_warning(
                        f"Attachment error for '{note_name}': {e}"
                    )

            note = Note(
                id=meta["id"],
                name=note_name,
                folder=folder.name,
                html_body=html_body,
                creation_date=meta["creation_date"],
                modification_date=meta["modification_date"],
                attachments=attachments,
            )
            notes.append(note)

    return notes
