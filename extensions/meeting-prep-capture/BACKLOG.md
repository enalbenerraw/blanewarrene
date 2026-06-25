# Meeting Prep Capture backlog

Items to address before publishing the extension to the Chrome Web Store.

## Before publishing

- [ ] **Fix the surface mismatch.** The popup hands off to `claude.ai/new`, but the plugin is a Claude Code / Cowork marketplace plugin, so a user (even a paying subscriber) who pastes into claude.ai web gets the degraded plain-Claude experience. Either point the handoff at the surface where the plugin actually lives, or make `blanewarrene.com/plugins` give clear per-surface install instructions so people paste in the right place.

- [ ] **Carry the upsell into the packet.** The "Need the brief generator" CTA lives in the popup, which is already closed by the time the user sees the thinner plain-Claude answer. Add a one-line footer to the handoff packet itself (e.g. "This is a lite prep. The full brief and one-pager come from the plugin at blanewarrene.com/plugins") so the pitch travels with the output into the chat. Tune how much profile text the packet hands over, since richer text narrows the lite-vs-full gap being monetized.

## Depends on

- A live `blanewarrene.com/plugins` page (the `Page — Plugins` pattern is built; needs the zip upload + page creation per the site's DEPLOY.md).
- Chrome Web Store listing (one-time $5 dev fee, MV3 review).
