# Rollout calendar: Product in Acquisitions OS launch

Two-week staggered launch. Week 1 is the public hook and free executive briefing. Week 2 is the premium offer to people who showed up. The long-form 17-page framework is the depth reward linked from inside the briefing, not the magnet itself.

**Week 1 publish date: Tuesday, 2026-06-02.**
**Week 2 publish date: Tuesday, 2026-06-09.**

## Pre-launch: Monday, 2026-06-01

| When | Asset | Action |
|------|-------|--------|
| Mon AM | Briefing PDF | Confirm `Product-in-Acquisitions-Executive-Briefing.pdf` is attached to the `pia-v0.1.0` GitHub release. Test the `/releases/download/pia-v0.1.0/...` URL in an incognito browser. |
| Mon AM | Long-form PDF | Confirm `The-90-Day-Product-Integration-Framework.pdf` is still attached to the same release. Test that URL too. |
| Mon AM | Substack welcome email | Paste copy from `welcome-email.md` into Substack Settings → Email → Welcome email. Test by subscribing with a throwaway address. Verify both PDF links resolve from the email. |
| Mon AM | Substack premium tier | Confirm the paid subscription is active and the price is set. |
| Mon AM | Website CTA | Add the hero CTA from `website-cta.md` to blanewarrene.com pointing at the Substack subscribe URL. |
| Mon PM | Substack post draft | Paste `articles/2026-05-05-the-gap-nobody-owns.md` into Substack. Wire CTAs to actual subscribe button and premium upgrade button. Schedule for 2026-06-02 at 8:00 AM ET. |

## Week 1: Public article + free briefing

| Date / Time | Asset | Action |
|-------------|-------|--------|
| Tue 2026-06-02 · 8:00 AM ET | Substack article | "The Gap Nobody Owns" goes live. Email goes out automatically. |
| Tue 2026-06-02 · 9:00 AM ET | LinkedIn | Post the LinkedIn version from `social-posts.md` (Week 1). |
| Tue 2026-06-02 · 11:00 AM ET | X | Post the X thread from `social-posts.md` (Week 1). |
| Tue 2026-06-02 · 1:00 PM ET | Facebook | Post the Facebook version from `social-posts.md` (Week 1). |
| Wed 2026-06-03 | Substack notes | Drop a Substack Note quoting the sharpest line ("the gap nobody owns" or the standup silence). |
| Thu 2026-06-04 | LinkedIn comment engagement | Reply to comments on Tuesday's LinkedIn post. Post one comment-thread follow-up if traction warrants. |
| Fri 2026-06-05 | Reshare check | Look at signups, top engagement, top reply. Reply to anyone who shared a real integration story. |

## Week 2: Plugin announcement to premium

| Date / Time | Asset | Action |
|-------------|-------|--------|
| Mon 2026-06-08 | Plugin announcement draft | Final read-through of `announcements/v0.1.0-substack.md`. Confirm the public article URL is correct in footnote [2]. Schedule for 2026-06-09 at 8:00 AM ET, **paid-only audience**. |
| Tue 2026-06-09 · 8:00 AM ET | Substack premium post | "The working version of last week's framework" goes out to premium subscribers only. |
| Tue 2026-06-09 · 9:00 AM ET | Public teaser post (optional) | Optional: a short Substack note (free + paid) saying "the plugin is live for premium" with a one-line teaser and an upgrade button. Drives last-chance free-to-paid conversion. |
| Tue 2026-06-09 · 10:00 AM ET | LinkedIn | Post the LinkedIn version from `social-posts.md` (Week 2). |
| Tue 2026-06-09 · 12:00 PM ET | X | Post the X version from `social-posts.md` (Week 2). |
| Tue 2026-06-09 · 2:00 PM ET | Facebook | Post the Facebook version from `social-posts.md` (Week 2). |
| Wed-Fri 2026-06-10 to 2026-06-12 | Field feedback watch | Watch GitHub Issues and email for first plugin reactions. Reply within 24 hours. |

## Post-launch

| Date | Action |
|------|--------|
| Fri 2026-06-12 | Audit signups, free-to-paid conversion rate, briefing downloads, long-form downloads, plugin downloads (GitHub release asset stats). |
| Week of 2026-06-15 | Decide whether the next post extends the framework series (e.g., a deep-dive on one lever) or pivots to a different topic. Target Tuesday 2026-06-23 for next major post if continuing. |
| Ongoing | Field feedback feeds the v0.1.1 plugin release. Cut the new tag when you have enough signal. The release workflow now bundles the framework PDF automatically. |

## Links to wire (collect once, paste everywhere)

- **Public article URL** (after publish): `https://blanewarrene.substack.com/p/the-gap-nobody-owns`
- **Premium announcement URL** (after publish): `https://blanewarrene.substack.com/p/...`
- **Subscribe URL**: `https://blanewarrene.substack.com/subscribe`
- **Premium upgrade URL**: `https://blanewarrene.substack.com/subscribe?type=paid`
- **Briefing PDF download** (the magnet): `https://github.com/enalbenerraw/blanewarrene/releases/download/pia-v0.1.0/Product-in-Acquisitions-Executive-Briefing.pdf`
- **Long-form framework PDF** (depth reward, linked inside the briefing): `https://github.com/enalbenerraw/blanewarrene/releases/download/pia-v0.1.0/The-90-Day-Product-Integration-Framework.pdf`
- **Plugin download**: `https://github.com/enalbenerraw/blanewarrene/releases/download/pia-v0.1.0/product-in-acquisitions-os.plugin`
- **GitHub repo**: `https://github.com/enalbenerraw/blanewarrene`

## Risks to watch

- **Marketing URLs are pinned to `pia-v0.1.0`.** This repo hosts multiple plugins, so `/releases/latest/` resolves to whichever plugin released most recently, not necessarily PIA. The fix is tag-specific URLs (`/releases/download/pia-v0.1.0/...`). When a future PIA release ships (`pia-v0.1.1`, etc.), bump the tag in every URL in this folder before the next post goes out. The release workflow now bundles both PDFs on every `pia-v*` tag, so the assets will exist; only the tag in the URL needs updating.
- **Briefing PDF asset on `pia-v0.1.0`.** The release was cut before the briefing existed, so the briefing must be uploaded manually to the `pia-v0.1.0` release as a one-time step. Verify it resolves at `https://github.com/enalbenerraw/blanewarrene/releases/download/pia-v0.1.0/Product-in-Acquisitions-Executive-Briefing.pdf` before Mon 2026-06-01.
- **Substack welcome email lag.** Welcome emails sometimes take 5-10 minutes. If subscribers are unhappy, mention "check spam, give it a few minutes" in the article CTA.
- **Premium leaks.** The plugin URL is public on GitHub. Some readers will figure out they can grab it without paying. Accept this. The premium tier sells the support, the templates roadmap, and the relationship, not the bytes.
- **Briefing-vs-long-form confusion.** Some subscribers will expect the long-form by default and feel shortchanged by a deck. The welcome email and the briefing itself both link to the long-form, so the depth signal is preserved if anyone goes looking. Watch reply volume in Week 1 for confusion signals; if it surfaces, add a one-line clarification to the welcome email.
