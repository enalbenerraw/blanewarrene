# Delivering artifacts durably

Every named deliverable a Product in Acquisitions OS skill produces is an external-grade work product. The user will share these with exec teams, acquisition committees, and boards. Do not leave them inline in the chat transcript only. Save each as its own self-contained file in a single run folder for the session, then tell the user where they are.

## Run folder

Create one folder for this skill run. The calling skill gives you the folder name (for example `<deal-slug>-week-0`). Derive `<deal-slug>` from the acquirer and acquired code names captured during context setup. Fall back to `acquisition` if neither was given.

## One file per deliverable

Write each deliverable as its own markdown file inside the run folder. The calling skill lists the filenames. Open every file with a short metadata header so it reads without the conversation:

- Date
- Acquirer and acquired (code names are fine)
- Deal thesis in one line
- Which deliverable this is

## Choose the delivery mechanism by surface

Use the best durable mechanism the current session offers. Detect it from the tools available to you:

- Artifact rendering available (claude.ai web): emit each deliverable as its own artifact so the user can share or fork it.
- File presentation available (Cowork hosted session): write the run folder under `/mnt/user-data/outputs/` and surface the files with `present_files`. Lead with the gating or summary deliverable.
- Local Claude Code (local filesystem, no file presentation tool): write the run folder under `~/Documents/` and report the full path to the user.

If more than one applies, prefer the richest in that order. Never finish a skill with the deliverables living only in the chat transcript.

## Footer

End every file with the attribution footer the calling skill specifies.

Keep the conversation as the working space for questions, drafts, and critique. The files are the deliverables.
