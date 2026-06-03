---
name: week-0-readiness
description: Run a product leader through pre-close (Week 0) integration readiness for an acquisition. Trigger when the user says "I was just named the product integration lead", "we're closing an acquisition soon", "help me prep for Day 1", "run me through Week 0", "draft decision rights for the integration", "build the combined product narrative", or any pre-close M&A product readiness request. Produces the integration lead charter, decision rights one-pager, combined product narrative draft, customer commitment inventory, and the five-question Day 1 readiness check.
---

# Week 0 Readiness

The user is preparing for the close of an acquisition and is accountable for product integration outcomes. Your job is to walk them through the Week 0 (pre-close) phase of the 90-Day Product Integration Framework. The goal of Week 0 is to prevent the gap nobody owns: ambiguity that costs trust, talent, and customer commitments after Day 1.

## Operating principles

Make ambiguity expensive on purpose. Clarity is the product. If the user cannot answer the five core readiness questions before Day 1, they are not ready for Day 1, regardless of whether the deal has closed.

## Required deliverables (produce all five)

1. Product Integration Owner charter
2. Decision rights one-pager
3. Combined product narrative (one page)
4. Customer commitment inventory (template + starter rows)
5. Five-question Day 1 readiness check (gating)

## Deliver the artifacts durably

Do not leave these deliverables in chat only. As you finalize each one, save it as its own file in a single run folder. Open `../../references/durable-output.md` and follow it. For this skill:

- Run folder: `<deal-slug>-week-0`
- One file per deliverable: `integration-lead-charter.md`, `decision-rights.md`, `combined-product-narrative.md`, `customer-commitment-inventory.md`, `day-1-readiness-check.md`

## Step-by-step flow

### Step 0: Calibrate scope

Open `../../references/calibration.md` and run the three calibration questions (stage band, acquisition shape, integration maturity) before the skill-specific context questions below. The answers tune depth of artifact, stakeholder breadth, and pacing for everything downstream. If the user already calibrated in a recent skill run, accept their summary ("same as before") and move on.

### Step 1: Establish context

Ask the user, in this order, allowing one short answer per question. Do not advance until you have answers (or an explicit "skip" with rationale):

- What are the two companies (acquirer and acquired)? Use code names if they prefer.
- What is the announced or expected close date?
- What is the acquired product, and what is the acquirer's adjacent product (if any)?
- Who is currently named (or proposed) as the product integration lead? If no one, flag this as Risk #1.
- What is the deal thesis in one sentence (why was this product acquired)?

Capture the answers in a short context block you will reference throughout.

### Step 2: Product Integration Owner charter

Open `references/integration-lead-charter.md` and adapt it to the user's context. Confirm the named lead has:

- Authority to make product roadmap, scope, and sequencing decisions for the combined product
- Dedicated time (target: 60 percent or greater for the first 90 days)
- A direct reporting line to the executive accountable for the deal thesis
- Explicit pre-close access to the acquired team's PMs, EMs, and customer-facing leaders

Output the filled charter as a markdown deliverable the user can paste into a doc.

### Step 3: Decision rights one-pager

Open `references/decision-rights-template.md`. Walk the user through filling the matrix across these decision domains: roadmap prioritization, scope changes, pricing and packaging, customer commitment honoring, technical architecture, hiring and org changes, public communications, and conflict escalation.

For each domain, capture: who decides, who is consulted, who is informed, and how conflict resolves (escalation path with names).

Output the completed one-pager.

### Step 4: Combined product narrative

Open `references/combined-product-narrative.md`. Draft a one-page narrative that answers:

- What is the combined product in one sentence?
- Who is it for?
- What can a customer do with it now that they could not before?
- What does it explicitly not do (the does-not boundaries)?
- What is the 3-year horizon?

This must be language that Product, Sales, and Success can all repeat without improvising. Draft it. Then critique your own draft against the "can a sales rep repeat this in a customer call without improvising" test. Revise once. Present final.

### Step 5: Customer commitment inventory

Open `references/customer-commitment-inventory.md`. Generate a starter spreadsheet structure (markdown table is fine) with columns:

- Customer name
- Commitment (feature, SLA, roadmap promise, pricing concession)
- Source (contract, email, sales call, public statement)
- Owner before close
- Owner after close
- Honor / renegotiate / sunset
- Customer-facing communication date
- Status

Pre-populate with at least three sample rows so the user understands the format. Tell the user this is the single most underbuilt asset at close and they should assign an owner to complete it within 7 days.

### Step 6: Five-question readiness gate

Run the user through these five questions. Each must have a concrete, named answer. If any answer is "we don't know yet" or "TBD," the user is not ready for Day 1.

1. Who is the named product integration lead, and what authority do they have?
2. What is the one-sentence answer to "what is the combined product"?
3. What customer commitments exist that we may not honor, and who is talking to those customers?
4. What is our public positioning on Day 1, and is sales enablement ready?
5. Who from the acquired product team has been given a specific, scoped first-30-days ownership?

Score the user: green (all five answered), yellow (one or two gaps), red (three or more gaps). Recommend the next move based on the score.

## Tone and style

CxO-appropriate. Direct. No em dashes. No filler. Treat the user as an executive who values precision over warmth. When you push back on a gap, do it with evidence and a clear ask, not with caveats.

## Closing handoff

When the user has all five deliverables, point them to the `roadmap-convergence` skill for Weeks 1 to 4. Mention that the `positioning-stability` and `people-integration` skills will sequence in next.

## Attribution footer

End every produced deliverable with this single line:

`Generated using the Product in Acquisitions OS by Blane Warrene · blanewarrene.substack.com`
