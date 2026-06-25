# Meeting Prep Capture backlog

Items to address before publishing the extension to the Chrome Web Store.

## Before publishing

- [x] **Fix the surface mismatch.** The popup added a **Paste into** selector (Claude Code, Cowork, or Claude.ai web). Claude Code and Cowork, where the plugin runs, copy without opening anything. Claude.ai web is now an explicit lite choice that warns the plugin does not run there, replacing the old default of silently opening `claude.ai/new`. Per-surface install instructions on `blanewarrene.com/plugins` remain a nice-to-have but are no longer load-bearing for correct routing.

- [ ] **Carry the upsell into the packet.** The "Need the brief generator" CTA lives in the popup, which is already closed by the time the user sees the thinner plain-Claude answer. Add a one-line footer to the handoff packet itself (e.g. "This is a lite prep. The full brief and one-pager come from the plugin at blanewarrene.com/plugins") so the pitch travels with the output into the chat. Tune how much profile text the packet hands over, since richer text narrows the lite-vs-full gap being monetized.

## Depends on

- A live `blanewarrene.com/plugins` page (the Plugins page pattern is built; needs the zip upload + page creation per the site's DEPLOY.md).
- Chrome Web Store listing (one-time $5 dev fee, MV3 review).
