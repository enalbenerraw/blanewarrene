# Meeting Prep Capture backlog

Items to address before publishing the extension to the Chrome Web Store.

## Before publishing

- [x] **Fix the surface mismatch.** The popup added a **Paste into** selector (Claude Code, Cowork, or Claude.ai web). Claude Code and Cowork, where the plugin runs, copy without opening anything. Claude.ai web is now an explicit lite choice that warns the plugin does not run there, replacing the old default of silently opening `claude.ai/new`. Per-surface install instructions on `blanewarrene.com/plugins` remain a nice-to-have but are no longer load-bearing for correct routing.

- [x] **Carry the upsell into the packet.** The lite/web packet now ends with a one-line footer pointing to `blanewarrene.com/plugins`, so the pitch travels into the chat after the popup has closed. The footer is scoped to the lite/web surface only; Code and Cowork run the plugin and would be misled by it. The lite packet also trims the captured profile to ~1500 characters (vs the full ~6000 on the plugin surfaces) to keep the free path lighter than the paid one. Still pending: the footer links to `blanewarrene.com/plugins`, which must be live (see Depends on) or the CTA dead-links.

- [ ] **Create real icon artwork.** The manifest wires `icons/icon-{16,32,48,128}.png` (top-level `icons` and `action.default_icon`), currently solid-color placeholders so the extension loads and the package validates. Design branded icons at all four sizes (the 128x128 is the Chrome Web Store listing icon and gets the most scrutiny), drop them in `icons/` overwriting the placeholders, bump the manifest version, and re-tag `meeting-prep-v*`. The release workflow globs in any non-`.md` files, so new icons ship without workflow changes.

## Depends on

- A live `blanewarrene.com/plugins` page (the Plugins page pattern is built; needs the zip upload + page creation per the site's DEPLOY.md).
- Chrome Web Store listing (one-time $5 dev fee, MV3 review).
