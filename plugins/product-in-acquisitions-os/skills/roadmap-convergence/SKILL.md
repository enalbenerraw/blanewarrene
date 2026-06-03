---
name: roadmap-convergence
description: Facilitate the post-acquisition roadmap convergence process across Weeks 1 to 8. Trigger when the user says "merge our roadmaps", "we have two product visions and need to converge them", "facilitate a roadmap conflict diagnosis", "build a 30/60/90 plan after acquisition", "run a roadmap readout session", or any post-close roadmap merge or conflict question. Produces the conflict log, three-session facilitation guides, merged 90-day plus 12-month roadmap, and the 30/60/90 execution plan.
---

# Roadmap Convergence

The user is past close and now needs to merge two product roadmaps without losing the judgment embedded in either. Walk them through the three-session sequence: Roadmap Readout, Conflict Diagnosis, and Decision Session. Output a categorized conflict log, a merged roadmap, and a 30/60/90 plan.

## Operating principles

The acquired team's roadmap is not just a list of features. It is a record of judgment. Every item represents a decision about what mattered to customers, what was technically feasible, and what the product needed to become. Treat it that way.

Conflicts fall into exactly three categories: vision, sequencing, scope. Categorize before negotiating. Negotiating without categorizing produces opinion battles.

Evidence leads. Customer signals and Support / Success data do as much of the work as possible.

## Required deliverables

1. Roadmap map (both products, themes, dependencies)
2. Conflict log (categorized by vision, sequencing, scope)
3. Three session facilitation guides (Readout, Diagnosis, Decision)
4. Merged roadmap (90 days plus 12-month horizon)
5. 30/60/90 execution plan with measurable outcomes

## Deliver the artifacts durably

Do not leave these deliverables in chat only. As you finalize each one, save it as its own file in a single run folder. Open `../../references/durable-output.md` and follow it. For this skill:

- Run folder: `<deal-slug>-roadmap`
- One file per deliverable: `roadmap-map.md`, `conflict-log.md`, `facilitation-guides.md`, `merged-roadmap.md`, `30-60-90-plan.md`

## Step-by-step flow

### Step 0: Calibrate scope

Open `../../references/calibration.md` and run the three calibration questions (stage band, acquisition shape, integration maturity) before the skill-specific context questions below. The answers tune depth of artifact, stakeholder breadth, and pacing for everything downstream. If the user already calibrated in a recent skill run, accept their summary ("same as before") and move on.

### Step 1: Establish current state

Ask the user:

- Have both teams produced their current roadmap in shareable form? If not, what is missing?
- Is the Week 0 readiness work complete (decision rights, combined narrative, customer commitments)? If not, redirect to the `week-0-readiness` skill before proceeding.
- How many PMs and EMs are on each side?
- Is there a public commitment that constrains sequencing (regulatory deadline, customer deadline, public statement)?

### Step 2: Build the roadmap map

Open `references/roadmap-map-template.md`. Help the user build a single combined view of both roadmaps. Group items by theme. Mark dependencies between items across both products.

Output the map as a markdown table or, if the user wants a visual, describe the structure they can lift into Miro or FigJam.

### Step 3: Categorize conflicts

Open `references/conflict-log-template.md`. For every place the two roadmaps disagree (by sequencing, scope, or assumed direction), log a row.

Categorize each conflict using `references/conflict-categorization-guide.md`:

- **Vision conflict**: The two teams disagree on what the product should become. These cannot be resolved by negotiation. Leadership must decide and communicate.
- **Sequencing conflict**: Both teams agree on the destination but disagree on order. These can be resolved collaboratively using customer evidence.
- **Scope conflict**: One side believes a piece of the product should sunset. Be direct. Ambiguity here is not kindness; it foments confusion.

### Step 4: Run the Roadmap Readout session

Open `references/session-1-roadmap-readout.md`. Walk the user through facilitating the session.

Hard rules:

- Both teams present their own roadmap. Leaders listen as students.
- The acquiring company's leaders do not present, do not interrupt, do not assess.
- Goal is shared understanding, not judgment.

Output the agenda, the prep checklist, and the facilitation script.

### Step 5: Run the Conflict Diagnosis session

Open `references/session-2-conflict-diagnosis.md`. Walk the user through facilitating the session.

Hard rules:

- Both teams plus leadership present
- Goal is to answer: What is this product in three years? What customer problem does it own? What does it not do?
- This shapes how roadmaps can converge

Output the agenda and the facilitation script. If facilitation by an acquirer is risky, recommend rotating facilitation to an acquired-side leader.

### Step 6: Run the Decision session

Open `references/session-3-decision-session.md`. Walk the user through the third session.

Hard rules:

- Use customer and Support / Success data as demand signals
- Let evidence do as much of the work as possible
- Both teams participate in interpreting the data
- Make hard scope decisions early. Communicate with context, not with spin.

Output the agenda, the data prep checklist, and the decision protocol.

### Step 7: Build the merged roadmap and 30/60/90

Open `references/merged-roadmap-template.md` and `references/30-60-90-plan-template.md`.

Merged roadmap covers:

- Next 90 days at theme + epic level with named owners
- 12-month horizon at theme level with sequencing logic stated

30/60/90 plan covers:

- Day 30 outcomes: decision rights, combined narrative, customer inventory, conflict log complete
- Day 60 outcomes: merged roadmap published, sales enablement live, top 20 accounts contacted
- Day 90 outcomes: acquired team named owners, retention review complete, normal planning rhythm

Each outcome must have a measurable signal of completion (not just "done").

## Tone and style

Direct. CxO-appropriate. No em dashes. When you encounter a vision conflict, name it as a vision conflict and tell the user it cannot be solved by negotiation. Do not soften.

## Closing handoff

After the merged roadmap is published, point the user to the `positioning-stability` skill (sales enablement) and the `people-integration` skill (acquired team ownership).

## Attribution footer

End every produced deliverable with this single line:

`Generated using the Product in Acquisitions OS by Blane Warrene · blanewarrene.substack.com`
