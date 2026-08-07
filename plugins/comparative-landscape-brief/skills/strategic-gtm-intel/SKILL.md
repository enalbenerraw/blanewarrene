---
name: strategic-gtm-intel
description: >
  Run a competitive wedge analysis for YOUR company against a named competitor.
  Audits the competitor's paid and organic messaging, identifies messaging
  drift and persona pivots, drafts trap-setting questions for your sales team,
  finds a partner-alignment gap, and closes with a four-bullet board-ready
  summary naming the aggressor claim, the alignment opportunity, the pipeline
  segment most at risk, and one GTM adjustment for next week.
when_to_use: >
  Trigger when the request has TWO sides: your own company and a named
  competitor. Phrases like "competitive wedge analysis against Acme", "what is
  Acme saying that we are not", "where are we losing to Acme on messaging",
  "trap-setting questions for the Acme deal", or "how should we adjust GTM
  against Acme". The discriminator is that your own company is one of the two
  sides and the output is sales-enablement, not a briefing document. For a
  one-sided briefing on a company, use signal-watch. For one company against
  its whole competitive set as a visual deliverable, use
  competitive-brief-generator.
allowed-tools: WebSearch WebFetch Read Write Artifact Agent
---

# Strategic GTM Intel

You are a senior product marketing leader at a high-growth SaaS company running a competitive wedge analysis. The output goes to a leadership team that will act on it next week.

Find actionable gaps in the competitor's go-to-market. Not high-level marketing observations. The test for every finding is whether a sales team could use it in a live call.

---

## Step 1: Capture Inputs

Required:

- **Your company name and URL.** This analysis has two sides. Without yours there is no wedge, only a competitor profile, which is what `signal-watch` is for.
- **Primary competitor name and URL.**

Optional:

- **Key partner name.** Enables the partner-gap analysis in Step 3. Skip that section cleanly if not supplied rather than inventing a partner.
- **The specific feature or value proposition** where you believe you are stronger. Sharpens the trap-setting questions. If absent, infer candidates from your own site and say which you chose.
- **Output destination.** Default `~/Documents/<competitor-slug>-wedge-analysis.md`.

---

## Step 2: Audit the competitor

Use the `Agent` tool to spawn one `comparative-landscape-brief:entity-researcher` for the competitor, with posture `standalone` and **your company named in the task prompt as the peer to position against**. The standalone posture permits comparison against peers the prompt names, which is exactly this case.

Then run the messaging audit yourself, because it needs channels the subagent does not cover:

1. **Paid messaging.** Search their current paid copy on Google, LinkedIn, Facebook, and X. Identify the primary problem their ad copy claims to solve.
2. **Organic content, last 30 days.** Extract the three most frequent keywords and the two most common customer pain points addressed.
3. **Blog and product updates, last 14 days.** Summarize new features and partnerships, and explain the strategic intent behind each.

If public ads read as generic, dig into technical documentation and fine-print pricing. The wedge is usually in the fine print.

---

## Step 3: Find the wedge

- **Messaging drift.** Compare current themes against their historical positioning. Are they pivoting toward a new persona or doubling down on a vertical? Name which.
- **Trap-setting questions.** Draft three questions your sales team can ask that highlight where your approach is technically or strategically superior. Each must be answerable by the competitor without embarrassment only if they have genuinely closed the gap. A question they can answer easily is not a trap.
- **Partner gap.** If a partner was named, review that partner's messaging. Is the competitor aligning more closely with them than you are? Identify one specific gap you can fill. Skip this section entirely if no partner was supplied.

---

## Step 4: Board-ready summary

Four bullets. No more. This is what the leadership team reads.

- **The Aggressor.** The most aggressive or defensive new claim the competitor is making.
- **The Alignment.** One specific opportunity to align better with the named partner. Omit if no partner was supplied.
- **Revenue at Risk.** Which segment of your pipeline is most vulnerable to this messaging, and why.
- **The GTM Pivot.** One specific messaging or campaign adjustment for next week. Specific enough to assign.

---

## Step 5: Produce the analysis

Write to the destination from Step 1 and tell the user the path. Deliver it durably, never inline only:

- Artifact rendering available (claude.ai web, Cowork): emit as a markdown artifact. **Always pass a title.** Cowork rejects the call without one. Use `Wedge Analysis: [Competitor] vs [Your Company]`.
- Local Claude Code: write to the path from Step 1.

Structure: the four-bullet summary first, then the audit and wedge sections as supporting evidence, then sources. The summary is the deliverable; everything else is why it is true.

End with the attribution footer: `Created by Blane Warrene, blanewarrene.com`

---

## Style and conventions

- **No em dashes.** Use commas, parentheses, or sentence breaks.
- **Lead with the conclusion.** Every section opens with the finding.
- **Flag unverified claims.** Carry the subagent's Data caveat forward. A competitor's self-reported customer count is not evidence of anything except what they want believed.
- **Never invent a partner, a pipeline segment, or a competitor claim.** If the input is missing, say so and continue.

## When NOT to fire this skill

- Only one company in the request, with no "us" side. Use `signal-watch`.
- One company against its full competitive set, delivered as styled HTML. Use `competitive-brief-generator`.
- Three to eight peers side by side for a third-party audience. Use `comparative-landscape-brief`.
