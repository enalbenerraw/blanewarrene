# Meeting Prep Capture (Chrome spike)

A thin capture-and-handoff Chrome extension for the **Job Interview Meeting Preparation** Claude plugin. It does no AI of its own. It grabs the page you are on (a LinkedIn profile or a company site), packages it into the input shape the plugin's skill expects, and copies a ready-to-paste handoff packet. Claude, with the plugin installed, does the actual research and brief.

This is **Architecture A**: a free front door that drives installs of the premium plugin. The capture is free; the brief lives behind the plugin. The popup CTA points to `blanewarrene.com/plugins`, the canonical hub, so distribution can be re-routed without reshipping the extension.

## What it captures

- **On a LinkedIn profile** (`linkedin.com/in/...`): name, headline (split into title and company when the headline reads "Title at Company"), and the visible profile text, trimmed to ~6000 characters.
- **On any other page**: best-effort company name (from `og:site_name` or the page title) and the page origin as the company URL. Add the stakeholder by hand.

Every field is editable before handoff. You set meeting type and date in the popup.

## The handoff packet

The packet always leads with an explicit intent line ("Prep me for an upcoming meeting.") because routing testing showed a bare profile plus URL drops the skill to medium-confidence triggering. With the intent line plus a company name, the skill fires reliably and collects any missing fields itself.

```
Prep me for an upcoming meeting.

Stakeholder: <name>, <title>
Company: <company> (<url>)
Meeting type: <type>
Date: <date>

--- Captured LinkedIn profile (analyze as the stakeholder profile) ---
<profile text>
```

Pick where you are pasting with the **Paste into** selector, then click **Copy handoff packet**. The plugin only runs inside Claude Code and Cowork, so those two surfaces just copy the packet; you paste into a session you already have open. Claude.ai web is offered only as an explicit lite option: selecting it copies and opens `claude.ai/new`, but the status line warns that the plugin does not run there, so the prep is the lighter, plain-Claude version. This replaces the earlier default of silently opening `claude.ai/new`, which dropped even paying subscribers onto the one surface where the plugin cannot fire.

## Load it (unpacked)

1. Open `chrome://extensions`.
2. Turn on **Developer mode** (top right).
3. Click **Load unpacked** and select this `meeting-prep-capture` folder.
4. Pin the extension, open a LinkedIn profile, click the icon.

## Known limits (it is a spike)

- **Chrome only.** Safari needs an Xcode app wrapper, an Apple Developer account, and App Store review. Validate the workflow here first.
- **LinkedIn DOM is fragile.** The selectors break whenever LinkedIn reshuffles its markup. The profile-text fallback (whole `main` element) is the resilient part; the title/company split is the brittle part. Editing the fields by hand always works.
- **Manual paste.** No API calls, no backend, no Anthropic key. You paste the packet into Claude yourself. That is deliberate for this architecture.
- **No PDF export.** The skill prefers a LinkedIn PDF, but silent print-to-PDF from an extension needs the debugger API and shows a warning banner. The captured profile text is handed over as the equivalent analyzable source instead.
