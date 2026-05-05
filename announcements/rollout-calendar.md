# Rollout calendar: Product in Acquisitions OS launch

Two-week staggered launch. Week 1 is the public hook and free magnet. Week 2 is the premium offer to people who showed up.

**Week 1 publish date: Tuesday, 2026-05-12.**
**Week 2 publish date: Tuesday, 2026-05-19.**

## Pre-launch: Monday, 2026-05-11

| When | Asset | Action |
|------|-------|--------|
| Mon AM | Framework PDF | Confirm the PDF is live at the stable URL (already done; it is on the v0.1.0 GitHub release). Test the download link in an incognito browser. |
| Mon AM | Substack welcome email | Paste copy from `welcome-email.md` into Substack Settings → Email → Welcome email. Test by subscribing with a throwaway address. |
| Mon AM | Substack premium tier | Confirm the paid subscription is active and the price is set. |
| Mon AM | Website CTA | Add the hero CTA from `website-cta.md` to blanewarrene.com pointing at the Substack subscribe URL. |
| Mon PM | Substack post draft | Paste `articles/2026-05-05-the-gap-nobody-owns.md` into Substack. Wire CTAs to actual subscribe button and premium upgrade button. Schedule for 2026-05-12 at 8:00 AM ET. |

## Week 1: Public article + free framework

| Date / Time | Asset | Action |
|-------------|-------|--------|
| Tue 2026-05-12 · 8:00 AM ET | Substack article | "The Gap Nobody Owns" goes live. Email goes out automatically. |
| Tue 2026-05-12 · 9:00 AM ET | LinkedIn | Post the LinkedIn version from `social-posts.md` (Week 1). |
| Tue 2026-05-12 · 11:00 AM ET | X | Post the X thread from `social-posts.md` (Week 1). |
| Tue 2026-05-12 · 1:00 PM ET | Facebook | Post the Facebook version from `social-posts.md` (Week 1). |
| Wed 2026-05-13 | Substack notes | Drop a Substack Note quoting the sharpest line ("the gap nobody owns" or the standup silence). |
| Thu 2026-05-14 | LinkedIn comment engagement | Reply to comments on Tuesday's LinkedIn post. Post one comment-thread follow-up if traction warrants. |
| Fri 2026-05-15 | Reshare check | Look at signups, top engagement, top reply. Reply to anyone who shared a real integration story. |

## Week 2: Plugin announcement to premium

| Date / Time | Asset | Action |
|-------------|-------|--------|
| Mon 2026-05-18 | Plugin announcement draft | Final read-through of `announcements/v0.1.0-substack.md`. Confirm the public article URL is correct in footnote [2]. Schedule for 2026-05-19 at 8:00 AM ET, **paid-only audience**. |
| Tue 2026-05-19 · 8:00 AM ET | Substack premium post | "The working version of last week's framework" goes out to premium subscribers only. |
| Tue 2026-05-19 · 9:00 AM ET | Public teaser post (optional) | Optional: a short Substack note (free + paid) saying "the plugin is live for premium" with a one-line teaser and an upgrade button. Drives last-chance free-to-paid conversion. |
| Tue 2026-05-19 · 10:00 AM ET | LinkedIn | Post the LinkedIn version from `social-posts.md` (Week 2). |
| Tue 2026-05-19 · 12:00 PM ET | X | Post the X version from `social-posts.md` (Week 2). |
| Tue 2026-05-19 · 2:00 PM ET | Facebook | Post the Facebook version from `social-posts.md` (Week 2). |
| Wed-Fri 2026-05-20 to 2026-05-22 | Field feedback watch | Watch GitHub Issues and email for first plugin reactions. Reply within 24 hours. |

## Post-launch

| Date | Action |
|------|--------|
| Fri 2026-05-22 | Audit signup numbers, free-to-paid conversion rate, plugin downloads (GitHub release asset stats). |
| Week of 2026-05-25 | Memorial Day week in the US (Mon 2026-05-25). B2B audiences are softer; do not publish a major post. Light Substack Notes only. |
| Week of 2026-06-01 | Decide whether the next post extends the framework series (e.g., a deep-dive on one lever) or pivots to a different topic. Target Tuesday 2026-06-02 for next major post if continuing. |
| Ongoing | Field feedback feeds the v0.1.1 plugin release. Cut the new tag when you have enough signal. The release workflow now bundles the framework PDF automatically. |

## Links to wire (collect once, paste everywhere)

- **Public article URL** (after publish): `https://blanewarrene.substack.com/p/the-gap-nobody-owns`
- **Premium announcement URL** (after publish): `https://blanewarrene.substack.com/p/...`
- **Subscribe URL**: `https://blanewarrene.substack.com/subscribe`
- **Premium upgrade URL**: `https://blanewarrene.substack.com/subscribe?type=paid`
- **Framework PDF download**: `https://github.com/enalbenerraw/blanewarrene/releases/latest/download/The-90-Day-Product-Integration-Framework.pdf`
- **Plugin download**: `https://github.com/enalbenerraw/blanewarrene/releases/latest/download/product-in-acquisitions-os.plugin`
- **GitHub repo**: `https://github.com/enalbenerraw/blanewarrene`

## Risks to watch

- **PDF link breaks at next release.** The release workflow now uploads the framework PDF on every tag, so the `/latest/` URL stays valid as long as the workflow runs successfully. If a future release fails the framework-PDF verification step, the v0.1.0 asset will still resolve through `/releases/latest/download/`.
- **Substack welcome email lag.** Welcome emails sometimes take 5-10 minutes. If subscribers are unhappy, mention "check spam, give it a few minutes" in the article CTA.
- **Premium leaks.** The plugin URL is public on GitHub. Some readers will figure out they can grab it without paying. Accept this. The premium tier sells the support, the templates roadmap, and the relationship, not the bytes.
