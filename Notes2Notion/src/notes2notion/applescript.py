"""AppleScript interface for Apple Notes.app via osascript."""

import subprocess
import sys
from typing import Any


TIMEOUT_SECONDS = 30
DELIMITER = "|||"
RECORD_DELIMITER = "^^^"


def _run_applescript(script: str, timeout: int = TIMEOUT_SECONDS) -> str:
    """Execute an AppleScript and return its stdout output."""
    try:
        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        raise TimeoutError("AppleScript timed out")
    except FileNotFoundError:
        print("Error: osascript not found. This tool requires macOS.", file=sys.stderr)
        sys.exit(1)

    if result.returncode != 0:
        raise RuntimeError(f"AppleScript error: {result.stderr.strip()}")

    return result.stdout.strip()


def check_access() -> bool:
    """Verify that Notes.app is accessible via AppleScript."""
    script = 'tell application "Notes" to return "ok"'
    try:
        return _run_applescript(script) == "ok"
    except (RuntimeError, TimeoutError):
        return False


def list_folders() -> list[dict[str, Any]]:
    """Return all folders in Notes.app with their note counts."""
    script = f'''
tell application "Notes"
    set output to ""
    repeat with f in every folder
        set fName to name of f
        set nCount to count of notes in f
        set output to output & fName & "{DELIMITER}" & nCount & "{RECORD_DELIMITER}"
    end repeat
    return output
end tell
'''
    raw = _run_applescript(script)
    if not raw:
        return []

    folders = []
    for record in raw.split(RECORD_DELIMITER):
        record = record.strip()
        if not record:
            continue
        parts = record.split(DELIMITER)
        if len(parts) >= 2:
            folders.append({
                "name": parts[0].strip(),
                "note_count": int(parts[1].strip()),
            })
    return folders


def list_notes_in_folder(folder_name: str) -> list[dict[str, str]]:
    """Return metadata for all notes in a given folder.

    Dates are emitted in ISO 8601 form (YYYY-MM-DD HH:MM:SS) built from
    numeric components, so the output does not depend on the system's
    locale-specific date formatting.
    """
    script = f'''
on pad2(n)
    set s to (n as string)
    if length of s < 2 then return "0" & s
    return s
end pad2

on isoDate(d)
    set y to (year of d) as string
    set mo to my pad2(month of d as integer)
    set dy to my pad2(day of d)
    set h to my pad2(hours of d)
    set m to my pad2(minutes of d)
    set s to my pad2(seconds of d)
    return y & "-" & mo & "-" & dy & " " & h & ":" & m & ":" & s
end isoDate

tell application "Notes"
    set output to ""
    set targetFolder to folder "{folder_name}"
    repeat with n in every note in targetFolder
        set nId to id of n
        set nName to name of n
        set nCreated to my isoDate(creation date of n)
        set nModified to my isoDate(modification date of n)
        set output to output & nId & "{DELIMITER}" & nName & "{DELIMITER}" & nCreated & "{DELIMITER}" & nModified & "{RECORD_DELIMITER}"
    end repeat
    return output
end tell
'''
    raw = _run_applescript(script, timeout=60)
    if not raw:
        return []

    notes = []
    for record in raw.split(RECORD_DELIMITER):
        record = record.strip()
        if not record:
            continue
        parts = record.split(DELIMITER)
        if len(parts) >= 4:
            notes.append({
                "id": parts[0].strip(),
                "name": parts[1].strip(),
                "creation_date": parts[2].strip(),
                "modification_date": parts[3].strip(),
            })
    return notes


def get_note_body(note_id: str) -> str:
    """Return the HTML body of a note by its ID."""
    script = f'''
tell application "Notes"
    set targetNote to first note whose id is "{note_id}"
    return body of targetNote
end tell
'''
    return _run_applescript(script, timeout=60)


def get_note_attachments(note_id: str) -> list[dict[str, str]]:
    """Return attachment info for a note."""
    script = f'''
tell application "Notes"
    set targetNote to first note whose id is "{note_id}"
    set output to ""
    repeat with a in every attachment of targetNote
        set aName to name of a
        set aId to id of a
        set output to output & aId & "{DELIMITER}" & aName & "{RECORD_DELIMITER}"
    end repeat
    return output
end tell
'''
    raw = _run_applescript(script, timeout=30)
    if not raw:
        return []

    attachments = []
    for record in raw.split(RECORD_DELIMITER):
        record = record.strip()
        if not record:
            continue
        parts = record.split(DELIMITER)
        if len(parts) >= 2:
            attachments.append({
                "id": parts[0].strip(),
                "name": parts[1].strip(),
            })
    return attachments
