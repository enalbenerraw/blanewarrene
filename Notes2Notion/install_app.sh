#!/bin/bash
# Install Notes2NotionUX as a macOS application in /Applications
#
# Usage: ./install_app.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE="$SCRIPT_DIR/Notes2NotionUX.applescript"
APP_PATH="/Applications/Notes2NotionUX.app"

if [ ! -f "$SOURCE" ]; then
    echo "Error: $SOURCE not found"
    exit 1
fi

# Remove existing app if present
if [ -d "$APP_PATH" ]; then
    echo "Removing existing $APP_PATH..."
    rm -rf "$APP_PATH"
fi

echo "Compiling Notes2NotionUX.app..."
osacompile -o "$APP_PATH" "$SOURCE"

echo "Installed to $APP_PATH"
echo "You can now launch Notes2NotionUX from Applications or Spotlight."
echo
echo "------------------------------------------------------------"
echo "REQUIRED: Grant Full Disk Access to export attachments"
echo "------------------------------------------------------------"
echo "Apple Notes keeps attachments in a protected location. Without"
echo "Full Disk Access, notes still export but every attachment is"
echo "skipped. Notes2NotionUX will warn you on launch if this is"
echo "missing, but you can set it up now:"
echo
echo "  1. Open System Settings > Privacy & Security > Full Disk Access"
echo "  2. Enable Notes2NotionUX (add it with + if it is not listed)"
echo "  3. Fully quit and reopen the app (the grant applies only to"
echo "     newly launched processes)"
echo
echo "Open that pane now with:"
echo "  open 'x-apple.systempreferences:com.apple.preference.security?Privacy_AllFiles'"
