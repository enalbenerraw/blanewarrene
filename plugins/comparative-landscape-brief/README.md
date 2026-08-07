# Market Intelligence

A Claude plugin for product and GTM leaders. Five skills share one hardened research subagent that verifies quantitative claims against third-party sources and refuses instructions embedded in fetched pages.

| Skill | Ask it when | Output |
|-------|-------------|--------|
| `comparative-landscape-brief` | 3 to 8 entities, side by side, for a third-party audience | Markdown brief |
| `signal-watch` | One company, understanding rather than preparing | Markdown brief |
| `competitive-brief-generator` | One company against its rivals, as a visual deliverable | Styled HTML, plus PDF |
| `strategic-gtm-intel` | Your company against one named competitor | Markdown, four-bullet board summary |
| `pre-call-briefing` | A commercial call already on the calendar | Markdown or memo, with a call playbook |

All five research companies, so routing matters. Each `when_to_use` names its discriminator and points at the others: entity count, whether your own company is one of the sides, whether a call is on the calendar, and output shape.

> The plugin directory and install name remain `comparative-landscape-brief`. Only the display name changed, so existing installs, the `clb-v*` release tags, and the stable Releases URL keep working.

## Comparative Landscape Brief

Researches a set of 3 to 8 organizations, products, or initiatives; analyzes the last 90 days of public messaging; verifies quantitative claims against third-party sources; and writes a single markdown brief ready for an investor call, board meeting, partner steering group, or M&A committee review.

The user is the presenter, not the audience. The brief is for someone else to read or to hear discussed.

## What it produces

A single markdown document with:

- A header (prepared date, audience, entity set, time window)
- Per-entity sections covering messaging themes over your chosen time window (90 days by default), inferred strategic priorities, and a leverageable tailwind
- Data caveats wherever third-party verification failed
- Cross-cutting observations useful at portfolio level
- Discussion prompts ready for the meeting
- A source set with hyperlinks

Saved by default to `~/Documents/<slug>-brief.md`. Set a different path with the output destination input.

## When to use it

Fire it when you need to compare a set of entities for an audience other than yourself. Examples:

- "Brief investors on what these six companies do and where each could go."
- "Compare these four vendors for the partner steering group."
- "Executive summary of the BOS category for our M&A committee."
- "Landscape brief on these competitors for the board."

## When NOT to use it

- **Single-entity research for your own prep.** Use the `job-interview-meeting-preparation` plugin instead.
- **Internal team retros or status updates.** Different shape.
- **Recurring competitive intelligence feeds.** This skill produces a static one-shot document.

## Inputs the skill will ask for

Required:

- Entity set (3 to 8 named organizations, products, or initiatives)
- Audience (investors, board, exec team, M&A committee, etc.)
- Purpose (the decision the brief informs)
- Lens (3 to 5 dimensions to compare on; the skill suggests defaults)
- Time window (default 90 days)

Optional:

- Output destination (file path)
- Tone (investor-grade default)
- Known angles to emphasize or de-emphasize

## Conventions

- No em dashes. Style rule enforced in CI.
- Direct, evidence-led tone. Peer-to-peer with the audience.
- Sources cited inline plus a closing source set.
- Every unverified quantitative claim is flagged with a Data caveat block.

## Install

### Marketplace

```bash
claude plugin marketplace add enalbenerraw/blanewarrene
claude plugin install comparative-landscape-brief@blanewarrene-marketplace
```

Run `/reload-plugins` afterward to apply it to a running session.

### Direct

Download the latest `comparative-landscape-brief.plugin` from the Releases page and drop it into the Claude plugin install panel.

## Author

Blane Warrene. [blanewarrene.com](https://blanewarrene.com)
