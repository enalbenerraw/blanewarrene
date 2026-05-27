# Scope Calibration

Run this once at the start of any skill in this plugin. It takes 60 seconds and tunes the depth, stakeholder breadth, and pacing of every deliverable Claude produces downstream. If the user has already answered these questions in a recent skill run, accept their summary ("same as before") and move on.

## Three questions to ask

Ask in order. One short answer each. Do not advance until all three are answered (or explicitly skipped with rationale).

1. **Stage band.** Sub-$100M ARR well-funded early stage, or $100M to $500M ARR mature growth stage?
2. **Acquisition shape.** Tuck-in (small team or tech absorbed into the acquirer), platform play (acquired company becomes the platform the acquirer builds on), or peer merger (two roughly equal products coming together)?
3. **Integration maturity.** Is this the acquiring team's first product integration, or have they run three or more before?

Capture the answers in a short calibration block. Reference it throughout the skill.

## Tuning levers

Apply these adjustments based on the answers above. When two signals conflict (e.g. sub-$100M but experienced acquirer), default to the deeper end of each lever; experienced acquirers ask for and absorb depth.

### Lever A: Depth of artifact

| Artifact | Sub-$100M / first integration | $100M-$500M / experienced |
|---|---|---|
| Decision rights one-pager | 5-7 roles | 12-14 roles (add Legal, Compliance, Finance, BU heads) |
| Customer commitment inventory | 10-25 rows; weekly cadence | 50-150+ rows; daily cadence in week 1 |
| Customer inventory composition (both bands) | Weight rows by risk segment, not by count. For tuck-ins, the standalone-product sunset cohort is the riskiest segment; over-represent it. For platform plays, the acquirer's top accounts hearing about scope changes is the riskiest segment. For peer mergers, customers with overlapping contracts on both sides. The right inventory tells the user where the fires are, not how many rows it has. | (same) |
| Sales FAQ | 8-10 questions | 15-20 questions (add procurement, security, regulatory) |
| Competitive response scripts | 3-5 plays | 5-7 plays (add segment-specific variants) |
| Top-N outreach | Top 20 named accounts | Top 50 named accounts, segmented by ARR band |
| Retention risk review | Per-person, narrative | Per-person scored on rubric, rolled up to function head |

### Artifacts that do NOT scale with calibration

The Product Integration Owner charter is universal. The mandate, authority structure, escalation path, and signature block are the same whether the acquirer is $40M ARR or $400M ARR. Only the *named reporting line* changes (CEO direct for sub-$100M; executive sponsor layer for $100M-$500M). Do not pad, trim, or restructure the charter based on stage band. Tune only the reporting line and the success-measure horizons (compressed 30/45/60 for sub-$100M tuck-ins; standard 30/60/90 otherwise).

### Lever B: Stakeholder breadth in facilitation

| Session | Sub-$100M / first integration | $100M-$500M / experienced |
|---|---|---|
| Roadmap Readout | One room: CEO, CPO, Heads of Eng/PM, 8-12 total | Structured rooms: exec sponsors, BU heads, PMM, Legal/Compliance observers, 15-25 total |
| Conflict Diagnosis | Same room, same people | Add Corp Dev, Finance partner, GTM lead |
| Decision Session | Decider + 4-6 advisors | Decider + decision council with documented votes |

### Lever C: Pacing

| Cadence | Sub-$100M tuck-in | Sub-$100M platform or peer | $100M-$500M (any shape) |
|---|---|---|---|
| Recommended rhythm | 30/45/60 (compressed) | 30/60/90 | 30/60/90 with optional 120-day governance lap |
| Combined narrative | One version, ships day 1 | One version, ships day 1, refreshed day 30 | Two versions: internal (day 1) and external-facing (day 14, post-listening tour) |
| Advisory council | Optional; informal customer calls may substitute | Lightweight, 8-12 customers, monthly | Formal charter, 12-20 customers, monthly with governance review at day 90 |

### Acquisition shape: language and framing

Independent of stage band, the acquisition shape changes how the combined product narrative is framed:

- **Tuck-in.** Lead with continuity. The acquirer's brand and product stay primary; the acquired capability becomes a named module or feature. Avoid language that elevates the acquired company beyond what customers will see.
- **Platform play.** Lead with the acquired product as the foundation. The acquirer's existing offerings layer on. This is the riskiest narrative because the acquirer's GTM team often defaults to old positioning; over-rehearse the new story.
- **Peer merger.** Lead with the new joint identity. Avoid either company's prior brand vocabulary. Customers on both sides need to hear what is genuinely new, not which side "won."

## How to apply during a skill run

After capturing the three answers, state back to the user one sentence that sets expectations. Example:

> "Calibrating for a $100M-$500M experienced platform play. I'll produce a 12-role decision rights matrix, a 50+ row customer commitment inventory starter, and frame the narrative around the acquired product as the foundation. Standard 30/60/90 pacing with a 120-day governance checkpoint."

Then proceed with the skill's Step 1. The skill-specific context questions stack on top of the calibration answers, not in place of them.

## When to recalibrate

If the user reports midway through that the deal shape changed (e.g. announced as tuck-in, now repositioned as platform play after Day 1 customer feedback), pause the current skill and rerun calibration. Update the calibration block and continue.
