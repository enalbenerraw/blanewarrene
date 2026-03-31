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
