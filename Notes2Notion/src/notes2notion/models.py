"""Data models for Notes2Notion."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Attachment:
    """An attachment belonging to an Apple Note."""

    original_path: Path
    filename: str
    media_type: str  # "image", "pdf", "other"
    note_id: str

    @property
    def output_filename(self) -> str:
        """Filename used in the export output."""
        return self.filename


@dataclass
class Note:
    """A single Apple Note with its content and metadata."""

    id: str
    name: str
    folder: str
    html_body: str
    creation_date: str
    modification_date: str
    attachments: list[Attachment] = field(default_factory=list)


@dataclass
class Folder:
    """A folder in Apple Notes containing notes."""

    name: str
    note_count: int = 0


@dataclass
class ExportConfig:
    """Configuration for a Notes2Notion export run."""

    output_dir: Path
    folders: list[str] | None = None  # None = all folders
    create_zip: bool = True
    created_within_days: int | None = None  # None = no date filter
