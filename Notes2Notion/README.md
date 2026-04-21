# Notes2Notion

A macOS tool that exports Apple Notes to Notion-importable Markdown files with full attachment support. Available as both a CLI and a native macOS GUI app.

## Features

- Export all notes or select specific folders
- Converts Apple Notes HTML to clean Markdown
- Full attachment support (images, PDFs, files)
- YAML frontmatter with metadata (title, dates, folder)
- Automatic ZIP packaging for Notion import
- Interactive CLI with progress tracking
- **Notes2NotionUX** — native macOS app with GUI dialogs (no Terminal required)

## Requirements

- macOS (Apple Notes.app access)
- Python 3.11+
- Terminal must have Automation permission for Notes.app (System Settings > Privacy & Security > Automation)

## Installation

```bash
cd Notes2Notion
pip install -e .
```

## Usage

### GUI App (Notes2NotionUX)

For users who prefer a graphical interface — no Terminal required.

**Install once:**

```bash
cd Notes2Notion
./install_app.sh
```

This compiles and installs `Notes2NotionUX.app` to `/Applications`. Launch it from Applications, Launchpad, or Spotlight.

The app presents native macOS dialogs to:
1. Select which folders to export (or all)
2. Choose where to save the output
3. Run the export with a progress notification
4. Show results and offer to reveal the ZIP in Finder

### CLI

```bash
notes2notion
```

The interactive CLI will guide you through:

1. **Folder selection** — export all notes or pick specific folders
2. **Output directory** — defaults to `~/Desktop/notes2notion_export`
3. **Export** — extracts notes, copies attachments, converts to Markdown
4. **ZIP creation** — produces a ready-to-upload ZIP file

### Batch Mode

For scripting or automation, run without interactive prompts:

```bash
# Export all folders
notes2notion --batch --all --output ~/Desktop/notes2notion_export

# Export specific folders
notes2notion --batch --folders "Work,Personal" --output ~/Desktop/my_export

# Only export notes created in the last 30, 90, or 180 days
notes2notion --batch --all --last-days 30 --output ~/Desktop/recent_export
```

### Importing into Notion

1. Open Notion > **Settings** > **Import**
2. Select **Markdown & CSV**
3. Upload the generated `.zip` file

## Output Format

```
notes2notion_export/
  assets/
    my-note_photo.jpg
    my-note_document.pdf
  My Note.md
  Another Note.md
  ...
```

Each Markdown file includes YAML frontmatter:

```yaml
---
title: "Note Title"
created: 2024-01-15 10:30:00
modified: 2024-03-20 14:22:00
folder: "Work"
---
```

## How It Works

1. Connects to Notes.app via AppleScript (`osascript`)
2. Enumerates folders and notes
3. Extracts HTML content and resolves attachments from `~/Library/Group Containers/group.com.apple.notes/Media/`
4. Converts HTML to Markdown using `markdownify`
5. Rewrites attachment paths and copies files to output
6. Packages everything into a Notion-ready ZIP

## Backlog

- [x] Filter notes by date range (last 30 / 90 / 180 days, by creation date)
- [ ] Surface date filter in the Notes2NotionUX GUI
- [ ] Selective note export within folders
- [ ] Direct Notion API import (skip ZIP upload)
- [ ] Add retry logic with backoff for AppleScript and file operations
