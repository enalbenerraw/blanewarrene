-- Notes2NotionUX — GUI wrapper for Notes2Notion
-- Provides native macOS dialogs for folder selection and output location,
-- then calls the Notes2Notion CLI in batch mode.

property appTitle : "Notes2NotionUX"
property cliPath : "/Users/blanewarrene/CLI_Work/blanewarrene/Notes2Notion/.venv/bin/notes2notion"

on run
	-- Step 1: Verify the CLI is installed
	try
		do shell script "test -f " & quoted form of cliPath
	on error
		display alert appTitle message "Notes2Notion CLI not found at:" & return & return & cliPath & return & return & "Please run 'pip install -e .' in the Notes2Notion directory first." as critical
		return
	end try

	-- Step 2: Get folder list from Notes.app
	set folderList to {}
	try
		tell application "Notes"
			repeat with f in every folder
				set end of folderList to name of f
			end repeat
		end tell
	on error errMsg
		display alert appTitle message "Could not connect to Notes.app:" & return & return & errMsg as critical
		return
	end try

	if (count of folderList) is 0 then
		display alert appTitle message "No folders found in Notes.app." as informational
		return
	end if

	-- Step 3: Folder selection dialog
	set folderChoices to {"All Notes"} & folderList
	set selectedItems to choose from list folderChoices with title appTitle with prompt "Select folders to export:" with multiple selections allowed

	if selectedItems is false then
		-- User cancelled
		return
	end if

	-- Step 4: Output location
	set outputFolder to choose folder with prompt "Choose where to save the export:"
	set outputPath to POSIX path of outputFolder
	set exportDir to outputPath & "notes2notion_export"

	-- Step 5: Build the CLI command
	set cliCmd to quoted form of cliPath & " --batch"

	if selectedItems contains "All Notes" then
		set cliCmd to cliCmd & " --all"
	else
		set folderArg to ""
		repeat with i from 1 to count of selectedItems
			if i > 1 then set folderArg to folderArg & ","
			set folderArg to folderArg & (item i of selectedItems)
		end repeat
		set cliCmd to cliCmd & " --folders " & quoted form of folderArg
	end if

	set cliCmd to cliCmd & " --output " & quoted form of exportDir

	-- Step 6: Show progress and run
	display notification "Export starting..." with title appTitle

	try
		set cmdOutput to do shell script cliCmd
	on error errMsg number errNum
		display alert appTitle message "Export failed:" & return & return & errMsg as critical
		return
	end try

	-- Step 7: Parse output for summary
	set notesExported to my extractValue(cmdOutput, "Notes exported: ")
	set attachmentCount to my extractValue(cmdOutput, "Attachments: ")
	set skippedCount to my extractValue(cmdOutput, "Skipped: ")
	set zipPath to my extractValue(cmdOutput, "ZIP: ")

	-- Step 8: Show completion dialog
	set summaryMsg to "Notes exported: " & notesExported & return & "Attachments: " & attachmentCount
	if skippedCount is not "" and skippedCount is not "0" then
		set summaryMsg to summaryMsg & return & "Skipped: " & skippedCount
	end if
	set summaryMsg to summaryMsg & return & return & "Output: " & exportDir
	if zipPath is not "" then
		set summaryMsg to summaryMsg & return & "ZIP: " & zipPath
	end if
	set summaryMsg to summaryMsg & return & return & "To import into Notion:" & return & "1. Open Notion > Settings > Import" & return & "2. Select \"Markdown & CSV\"" & return & "3. Upload the ZIP file"

	set userAction to button returned of (display dialog summaryMsg with title appTitle buttons {"Close", "Show in Finder"} default button "Show in Finder" with icon note)

	if userAction is "Show in Finder" then
		if zipPath is not "" then
			do shell script "open -R " & quoted form of zipPath
		else
			do shell script "open " & quoted form of exportDir
		end if
	end if
end run

on extractValue(sourceText, prefix)
	set AppleScript's text item delimiters to return
	set textLines to text items of sourceText
	set AppleScript's text item delimiters to ""
	repeat with aLine in textLines
		set aLine to aLine as text
		if aLine starts with prefix then
			return text ((length of prefix) + 1) thru -1 of aLine
		end if
	end repeat
	return ""
end extractValue
