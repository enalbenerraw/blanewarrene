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
- **Automation permission** for Notes.app, so the tool can read note text via AppleScript (System Settings > Privacy & Security > Automation)
- **Full Disk Access** for whatever runs the export, so it can resolve attachments

### Why Full Disk Access is required

Apple Notes stores attachment files and its index database (`NoteStore.sqlite`) inside `~/Library/Group Containers/group.com.apple.notes/`, a TCC-protected location. The scriptable note body does not contain attachment file references, so attachments can only be resolved by reading that container directly. Without Full Disk Access the export still runs and note text comes through, but **zero attachments are exported** and the tool prints a diagnostic explaining why.

Grant it under System Settings > Privacy & Security > Full Disk Access, then add the process that runs the export and relaunch it:

- Running the CLI: add your terminal app (Terminal.app, iTerm, etc.)
- Running the GUI: add `Notes2NotionUX.app`

The grant only applies to newly launched processes, so fully quit and reopen the terminal or app after enabling it.

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
2. Enumerates folders and notes, and extracts each note's HTML body
3. Resolves attachments through `NoteStore.sqlite`: each AppleScript attachment id carries a Core Data primary key, which is mapped to its media row (`ZMEDIA`) to find the file under `~/Library/Group Containers/group.com.apple.notes/Accounts/*/Media/<uuid>/`. AppleScript attachment names are unreliable (often empty), so this database join is the only robust path.
4. Converts HTML to Markdown using `markdownify`
5. Copies attachment files to `assets/`, embeds images and links other files at the end of each note (AppleScript does not expose where attachments sit inline)
6. Packages everything into a Notion-ready ZIP

## Backlog

- [x] Filter notes by date range (last 30 / 90 / 180 days, by creation date)
- [x] Resolve attachments via `NoteStore.sqlite` (replaces unreliable name matching)
- [x] **Notes2NotionUX: detect missing Full Disk Access before export** via a `notes2notion --check-access` preflight and a native dialog (Open Settings / Continue Without Attachments / Cancel), instead of silently producing an attachment-free export
- [ ] **Notes2NotionUX: document the Full Disk Access grant in `install_app.sh`** output, since the bundle (not Terminal) is the process that needs it when run as a GUI
- [ ] **Notes2NotionUX: surface per-note attachment warnings** in the results dialog (currently only visible on the CLI)
- [ ] Embed images inline at their original position (blocked: AppleScript does not expose attachment placement; would require parsing the note's protobuf body in `NoteStore.sqlite`)
- [ ] Surface date filter in the Notes2NotionUX GUI
- [ ] Selective note export within folders
- [ ] Direct Notion API import (skip ZIP upload)
- [ ] Add retry logic with backoff for AppleScript and file operations
