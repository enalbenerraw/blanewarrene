# Welcome email: free subscriber

*Triggered when someone subscribes to the free tier on Substack. Delivers the framework PDF.*

---

**Subject lines (pick one):**

- Your 90-Day Product Integration Framework is attached
- The framework, as promised
- Here is the framework

---

**Body:**

Welcome.

Attached is the 90-Day Product Integration Framework. 17 pages. Five levers, a week-by-week plan, and the reusable checklists I use on every integration I work through.

If you are running a deal right now, start with the Day 1 Readiness Checklist on page 16. Five questions. If you cannot answer them before Day 1, you are not ready for Day 1.

[Download the framework PDF][1]

A note on what to expect from this list:

- One post most weeks on product, GTM, and the work of building B2B SaaS at the leadership layer
- Specific, deal-tested frameworks where I have them
- No drip sequences, no upsells, no AI-generated filler

Premium subscribers also get the framework as a working Claude plugin with 25 templates that produce the actual deliverables (charters, FAQs, session guides, retention reviews) for your specific deal. If that is useful, the upgrade lives at the bottom of every post.

If you have a story from a real integration, hit reply. The next release of the framework folds in field signal from readers.

Blane
blanewarrene.com

[1]: https://github.com/enalbenerraw/blanewarrene/releases/latest/download/The-90-Day-Product-Integration-Framework.pdf

---

## Delivery notes

**For Substack:** the framework PDF is too large to attach to a Substack email reliably. Two options:

1. **Host the PDF on a public URL** (GitHub Releases, S3, Substack file upload) and link to it. Cleanest. Recommended.
2. **Embed in a Substack "welcome post"** that new subs are auto-routed to. Substack's welcome email can link to a Substack-hosted post that has the download button.

If hosting on GitHub: upload `The-90-Day-Product-Integration-Framework.pdf` as a release asset (separate release from the plugin, e.g., a `framework-v1.0` tag), then use the `/releases/latest/download/...` stable URL pattern. Or attach to the existing `v0.1.0` plugin release as a second asset.

**Substack Settings → Email → Welcome email** is where this copy goes. Make sure the link in [1] resolves before turning on the welcome flow.
