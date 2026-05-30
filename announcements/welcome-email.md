# Welcome email: free subscriber

*Triggered when someone subscribes to the free tier on Substack. Delivers the executive briefing deck.*

---

**Subject lines (pick one):**

- The 90-Day Product Integration Briefing is attached
- The briefing, as promised
- Here is the briefing

---

**Body:**

Welcome.

Attached is the 90-Day Product Integration Briefing. The five levers that decide post-acquisition outcomes, condensed for the people who need to make decisions before the deal closes.

[Download the briefing][1]

If you want the long-form version, the 17-page framework is linked at the bottom of this email. Start with the Day 1 Readiness Checklist on page 16. Five questions. If you cannot answer them before Day 1, you are not ready for Day 1.

A note on what to expect from this list:

- One post most weeks on product, GTM, and the work of building B2B SaaS at the leadership layer
- Specific, deal-tested frameworks where I have them
- No drip sequences, no upsells, no AI-generated filler

Premium subscribers also get the framework as a working Claude plugin with 25 templates that produce the actual deliverables (charters, FAQs, session guides, retention reviews) for your specific deal. If that is useful, the upgrade lives at the bottom of every post.

If you have a story from a real integration, hit reply. The next release of the framework folds in field signal from readers.

Blane
blanewarrene.com

[Download the briefing][1] · [Read the long-form (17 pages)][2]

[1]: https://github.com/enalbenerraw/blanewarrene/releases/download/pia-v0.2.0/Product-in-Acquisitions-Executive-Briefing.pdf
[2]: https://github.com/enalbenerraw/blanewarrene/releases/download/pia-v0.2.0/The-90-Day-Product-Integration-Framework.pdf

---

## Delivery notes

**For Substack:** the briefing PDF is small enough (~1.1 MB) that some email clients will accept it as an attachment, but link-hosting is still more reliable. Two options:

1. **Host both PDFs on a public URL** (GitHub Releases is the existing path). Cleanest. Recommended.
2. **Embed in a Substack "welcome post"** that new subs are auto-routed to. Substack's welcome email can link to a Substack-hosted post that has the download buttons.

Both `Product-in-Acquisitions-Executive-Briefing.pdf` and `The-90-Day-Product-Integration-Framework.pdf` are attached to the `pia-v0.2.0` GitHub release. The marketing URLs use tag-specific paths (`/releases/download/pia-v0.2.0/...`) instead of `/latest/` because this repo hosts multiple plugins and `/latest/` resolves to whichever plugin released most recently. When PIA cuts a new tag, update the tag in the URLs throughout this folder.

**Substack Settings → Email → Welcome email** is where this copy goes. Make sure the links in [1] and [2] resolve before turning on the welcome flow.
