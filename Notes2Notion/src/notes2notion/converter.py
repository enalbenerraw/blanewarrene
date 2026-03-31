"""HTML to Markdown conversion with Notion-optimized output."""

import re

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

from .models import Attachment, Note


class AppleNotesConverter(MarkdownConverter):
    """Custom markdownify converter tuned for Apple Notes HTML quirks."""

    def convert_div(self, el, text, **kwargs):
        """Convert <div> to paragraph (Apple Notes uses divs instead of p)."""
        return f"\n{text.strip()}\n\n" if text.strip() else ""

    def convert_br(self, el, text, **kwargs):
        return "\n"

    def convert_tt(self, el, text, **kwargs):
        """Convert <tt> (monospace) to inline code."""
        return f"`{text}`" if text else ""


def _build_attachment_map(attachments: list[Attachment]) -> dict[str, str]:
    """Map original filenames/paths to output asset paths."""
    mapping: dict[str, str] = {}
    for att in attachments:
        # Map by original filename
        mapping[att.original_path.name] = f"assets/{att.filename}"
        # Also map by full original path
        mapping[str(att.original_path)] = f"assets/{att.filename}"
        # Map file:// URL form
        mapping[f"file://{att.original_path}"] = f"assets/{att.filename}"
    return mapping


def _rewrite_attachment_refs(html: str, att_map: dict[str, str]) -> str:
    """Rewrite attachment references in HTML before markdown conversion."""
    soup = BeautifulSoup(html, "html.parser")

    for img in soup.find_all("img"):
        src = img.get("src", "")
        # Try full match, then filename-only match
        new_src = att_map.get(src)
        if new_src is None:
            src_clean = src.replace("file://", "")
            new_src = att_map.get(src_clean)
        if new_src is None:
            # Try matching just the filename
            from pathlib import Path
            fname = Path(src.replace("file://", "")).name
            new_src = att_map.get(fname)
        if new_src:
            img["src"] = new_src

    for obj in soup.find_all("object"):
        data = obj.get("data", "")
        new_data = att_map.get(data)
        if new_data is None:
            data_clean = data.replace("file://", "")
            new_data = att_map.get(data_clean)
        if new_data is None:
            from pathlib import Path
            fname = Path(data.replace("file://", "")).name
            new_data = att_map.get(fname)
        if new_data:
            # Convert <object> to <a> for markdown conversion
            link = soup.new_tag("a", href=new_data)
            link.string = obj.get("data-name", new_data.split("/")[-1])
            obj.replace_with(link)

    return str(soup)


def _generate_frontmatter(note: Note) -> str:
    """Generate YAML frontmatter for a note."""
    # Escape quotes in title
    safe_title = note.name.replace('"', '\\"')
    lines = [
        "---",
        f'title: "{safe_title}"',
        f"created: {note.creation_date}",
        f"modified: {note.modification_date}",
        f'folder: "{note.folder}"',
        "---",
        "",
    ]
    return "\n".join(lines)


def _clean_markdown(md: str) -> str:
    """Clean up markdown output."""
    # Collapse excessive blank lines
    md = re.sub(r"\n{3,}", "\n\n", md)
    # Strip trailing whitespace per line
    md = "\n".join(line.rstrip() for line in md.splitlines())
    # Ensure single trailing newline
    md = md.strip() + "\n"
    return md


def convert_note(note: Note) -> str:
    """Convert a Note to Notion-ready Markdown with frontmatter."""
    att_map = _build_attachment_map(note.attachments)

    # Rewrite attachment references before conversion
    html = _rewrite_attachment_refs(note.html_body, att_map)

    # Convert HTML to Markdown
    converter = AppleNotesConverter(
        heading_style="ATX",
        bullets="-",
        strong_em_symbol="*",
        strip=["style", "script", "meta"],
    )
    markdown_body = converter.convert(html)
    markdown_body = _clean_markdown(markdown_body)

    # Add any non-image attachments as links at the bottom
    non_image_attachments = [
        a for a in note.attachments if a.media_type != "image"
    ]
    if non_image_attachments:
        markdown_body += "\n## Attachments\n\n"
        for att in non_image_attachments:
            markdown_body += f"- [{att.filename}](assets/{att.filename})\n"

    frontmatter = _generate_frontmatter(note)
    return frontmatter + "\n" + markdown_body
