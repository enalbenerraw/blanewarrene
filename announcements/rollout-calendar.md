# Rollout calendar: Product in Acquisitions OS launch

Two-week staggered launch. Week 1 is the public hook and free magnet. Week 2 is the premium offer to people who showed up.

Pick a Tuesday for Week 1 publish (highest open rates for B2B Substack). Adjust dates below to your preferred Tuesday.

## Pre-launch (the day before Week 1)

| When | Asset | Action |
|------|-------|--------|
| Mon AM | Framework PDF | Confirm `The-90-Day-Product-Integration-Framework.pdf` is uploaded as a GitHub release asset (or wherever you choose to host it). Test the download link in an incognito browser. |
| Mon AM | Substack welcome email | Paste copy from `welcome-email.md` into Substack Settings → Email → Welcome email. Test by subscribing with a throwaway address. |
| Mon AM | Substack premium tier | Confirm the paid subscription is active and the price is set. |
| Mon AM | Website CTA | Add the hero CTA from `website-cta.md` to blanewarrene.com pointing at the Substack subscribe URL. |
| Mon PM | Substack post draft | Paste `articles/2026-05-05-the-gap-nobody-owns.md` into Substack. Wire CTAs to actual subscribe button and premium upgrade button. Schedule for Tuesday 8:00 AM ET. |

## Week 1: Public article + free framework

| When | Asset | Action |
|------|-------|--------|
| Tue 8:00 AM ET | Substack article | "The Gap Nobody Owns" goes live. Email goes out automatically. |
| Tue 9:00 AM | LinkedIn | Post the LinkedIn version from `social-posts.md` (Week 1). |
| Tue 11:00 AM | X | Post the X thread from `social-posts.md` (Week 1). |
| Tue 1:00 PM | Facebook | Post the Facebook version from `social-posts.md` (Week 1). |
| Wed | Substack notes | Drop a Substack Note quoting the sharpest line ("the gap nobody owns" or the standup silence). |
| Thu | LinkedIn comment engagement | Reply to comments on Tuesday's LinkedIn post. Post one comment-thread follow-up if traction warrants. |
| Fri | Reshare check | Look at signups, top engagement, top reply. Reply to anyone who shared a real integration story. |

## Week 2: Plugin announcement to premium

| When | Asset | Action |
|------|-------|--------|
| Mon | Plugin announcement draft | Final read-through of `announcements/v0.1.0-substack.md`. Confirm the public article URL is correct in footnote [2]. Schedule for Tuesday 8:00 AM ET, **paid-only audience**. |
| Tue 8:00 AM ET | Substack premium post | "The working version of last week's framework" goes out to premium subscribers only. |
| Tue 9:00 AM | Public teaser post (optional) | Optional: a short Substack note (free + paid) saying "the plugin is live for premium" with a one-line teaser and an upgrade button. Drives last-chance free-to-paid conversion. |
| Tue 10:00 AM | LinkedIn | Post the LinkedIn version from `social-posts.md` (Week 2). |
| Tue 12:00 PM | X | Post the X version from `social-posts.md` (Week 2). |
| Tue 2:00 PM | Facebook | Post the Facebook version from `social-posts.md` (Week 2). |
| Wed-Fri | Field feedback watch | Watch GitHub Issues and email for first plugin reactions. Reply within 24 hours. |

## Post-launch (Week 3+)

| When | Action |
|------|--------|
| End of Week 2 | Audit signup numbers, free-to-paid conversion rate, plugin downloads (GitHub release asset stats). |
| Week 3 | Decide whether the next post extends the framework series (e.g., a deep-dive on one lever) or pivots to a different topic. |
| Ongoing | Field feedback feeds the v0.1.1 plugin release. Cut the new tag when you have enough signal. |

## Links to wire (collect once, paste everywhere)

- **Public article URL** (after publish): `https://blanewarrene.substack.com/p/the-gap-nobody-owns`
- **Premium announcement URL** (after publish): `https://blanewarrene.substack.com/p/...`
- **Subscribe URL**: `https://blanewarrene.substack.com/subscribe`
- **Premium upgrade URL**: `https://blanewarrene.substack.com/subscribe?type=paid`
- **Framework PDF download**: `https://github.com/enalbenerraw/blanewarrene/releases/latest/download/The-90-Day-Product-Integration-Framework.pdf` (assuming you upload it to the same release)
- **Plugin download**: `https://github.com/enalbenerraw/blanewarrene/releases/latest/download/product-in-acquisitions-os.plugin`
- **GitHub repo**: `https://github.com/enalbenerraw/blanewarrene`

## Risks to watch

- **PDF link breaks.** If you upload the PDF to GitHub Releases, the `/latest/` URL changes when you cut a new tag. Either pin to a specific version (`/download/v0.1.0/`) or upload as a separate, never-tagged release.
- **Substack welcome email lag.** Welcome emails sometimes take 5-10 minutes. If subscribers are unhappy, mention "check spam, give it a few minutes" in the article CTA.
- **Premium leaks.** The plugin URL is public on GitHub. Some readers will figure out they can grab it without paying. Accept this. The premium tier sells the support, the templates roadmap, and the relationship, not the bytes.
