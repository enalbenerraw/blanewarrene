---
name: positioning-stability
description: Build the post-acquisition positioning, sales enablement, and customer outreach kit. Trigger when the user says "build a positioning statement after acquisition", "we have two sales reps telling different stories", "create a sales FAQ for the merged company", "draft a competitive response after acquisition", "set up an advisory council after the deal", "outreach plan for top accounts after close", or any post-close GTM coherence question. Produces the positioning statement, sales FAQ, talk track, competitive response scripts, top-20 outreach plan, and advisory council charter.
---

# Positioning Stability

Two sales reps showed up at the same prospect with different stories within 30 days of close. The prospect did not lose confidence in the product. They lost confidence in the company. Your job is to prevent that. Build the positioning, enablement, and outreach kit so the combined company speaks with one voice.

## Operating principles

Customers do not care about the competitive map. They care about their own problems and whether the company they are buying from understands those problems well enough to solve them.

The positioning question, properly framed: given what we now offer as a combined company, what can a customer do or achieve that they could not before?

Sales enablement must be ready at close, not 30 days after. If it is not ready at close, sales reps will improvise, and improvisation in the first 30 days is what destroys deals.

## Required deliverables

1. Positioning statement (one paragraph, customer outcome framed)
2. Sales FAQ (the 15 questions reps will get in the first 60 days)
3. Talk track (the 90-second version of the story)
4. Competitive response scripts (the 5 most likely competitor plays)
5. Top-20 outreach plan (named accounts, named senior leaders, scheduled in week 1-2)
6. Advisory council charter (lightweight, first 90 days)

## Deliver the artifacts durably

Do not leave these deliverables in chat only. As you finalize each one, save it as its own file in a single run folder. Open `../../references/durable-output.md` and follow it. For this skill:

- Run folder: `<deal-slug>-positioning`
- One file per deliverable: `positioning-statement.md`, `sales-faq.md`, `talk-track.md`, `competitive-response-scripts.md`, `top-20-outreach-plan.md`, `advisory-council-charter.md`

## Step-by-step flow

### Step 0: Calibrate scope

Open `../../references/calibration.md` and run the three calibration questions (stage band, acquisition shape, integration maturity) before the skill-specific context questions below. The answers tune depth of artifact, stakeholder breadth, and pacing for everything downstream. If the user already calibrated in a recent skill run, accept their summary ("same as before") and move on.

### Step 1: Establish context

Ask the user:

- Is the Combined Product Narrative from `week-0-readiness` complete? If not, redirect there first. Positioning depends on it.
- Who are the top 20 accounts on each side? (Acquirer + acquired)
- Who are the top 5 competitors who will use the acquisition against you?
- What public statements have already been made about the deal (press release, customer letter, blog)?

### Step 2: Build the positioning statement

Open `references/positioning-statement-worksheet.md`. Walk the user through the customer-outcome framing.

The statement must answer: given what we now offer as a combined company, what can a customer do or achieve that they could not before? In one paragraph, with no buzzwords.

Test the draft against three checks:

- Could a sales rep deliver this without improvising?
- Does it name a customer outcome, not a feature list?
- Would the acquired team's CEO recognize their company in this language?

Revise once. Present final.

### Step 3: Sales FAQ

Open `references/sales-faq-template.md`. Generate 15 questions sales reps will get in the first 60 days, with answers. Include:

- "Is the [acquired product] going away?"
- "Will my pricing change?"
- "Will my account team change?"
- "What happens to the [feature] you promised me?"
- "How does this compare to [competitor]?"
- "Should I wait to renew until things settle down?"
- "Are you going to integrate with our [tool]?"

Answers must use the language of the positioning statement and the combined product narrative.

### Step 4: Talk track

Open `references/talk-track-template.md`. The 90-second version of the story for use in customer calls, sales meetings, and conferences. Three sections:

- The setup (15 seconds): what changed and why it matters to the customer
- The substance (60 seconds): what the combined product does for the customer
- The next step (15 seconds): what the customer should do or expect

### Step 5: Competitive response scripts

Open `references/competitive-response-template.md`. Generate scripts for the five most likely competitor plays. Common patterns:

- "They were acquired and the product will languish"
- "They got rid of the founders and the vision is gone"
- "Pricing is going up, you should switch to us"
- "Their roadmap is now controlled by [acquirer], who has different priorities"
- "Acquisitions always lead to layoffs, support is going to suffer"

Each response is direct, grounded, brief. Three sentences max. No defensiveness.

### Step 6: Top-20 outreach plan

Open `references/top-20-outreach-plan.md`. Build the plan to get the most senior product and GTM leaders on calls with the top 20 accounts on both sides in the first two weeks.

The point is not to sell. The point is to listen and demonstrate through the quality of attention that the relationship matters. Acquired customers especially need to hear directly from senior leadership, without spin.

Output: named account list, named senior leader for each call, scheduling owner, talking points (not a script), follow-up commitment.

### Step 7: Advisory council charter

Open `references/advisory-council-charter.md`. Set up a lightweight council of 8 to 12 customers (mix of acquirer and acquired) for the first 90 days. They become your most reliable source of positive market signals.

Output: charter, member criteria, cadence (recommend monthly for first 90 days, then quarterly), commitments from the company, commitments from the members.

## Tone and style

CxO-appropriate. Direct. No em dashes. When you draft customer-facing language, default to plain English over marketing language. Read every draft through the question: would a CxO at the customer roll their eyes at this?

## Closing handoff

After the kit ships, point the user to the `people-integration` skill (acquired team belonging) if they have not already started it.

## Attribution footer

End every produced deliverable with this single line:

`Generated using the Product in Acquisitions OS by Blane Warrene · blanewarrene.substack.com`
