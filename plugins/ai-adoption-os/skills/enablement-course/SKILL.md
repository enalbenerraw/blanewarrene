---
name: enablement-course
description: >
  Assemble an internal AI enablement course for a company's own employees,
  sized to where they actually are rather than where a vendor deck assumes they
  are. Produces the session plan, per-session content and exercises, a
  facilitator guide for a non-expert, and a way to tell whether it worked.
  Builds on the tech stack inventory, readiness survey, and prompt cookbook
  where those exist.
when_to_use: >
  Trigger when an operator needs to teach their own staff to use AI. Phrases
  like "build an internal AI training course", "how do I roll out AI training",
  "our team has Claude seats and needs onboarding", "internal AI enablement
  program", or "train the team without hiring a consultant". The discriminator
  is INTERNAL training for employees. For a public, sellable course for
  customers, use the Teachable Course Builder prompt instead. To build the
  prompts the course teaches, use prompt-cookbook first.
allowed-tools: WebSearch WebFetch Read Write AskUserQuestion Artifact
---

# Enablement Course

You are building an internal AI enablement course for a 25 to 150 person company, to be run by someone who is not an AI expert and has a day job.

**This is internal enablement, not a product.** Nobody buys it, nobody markets it, and its only measure of success is whether people use AI differently afterward. If the user wants a public course to sell, route to the Teachable Course Builder prompt.

---

## Step 1: Interview

Use `AskUserQuestion`.

1. **Who is being trained.** Everyone, one function, or managers first. Determines the whole shape.
2. **Starting point.** Never used AI, using it informally, or already using it and doing it badly. **This is the question most training gets wrong**, because a course built for beginners bores the people already using AI and loses them permanently.
3. **Format they can actually run.** Live sessions, recorded, self-serve written, or a mix. Constrained by whether anyone has time to facilitate.
4. **Time available.** Per session and in total. Be blunt that a four-hour program at a 40-person company usually means four one-hour sessions, not a workshop day.
5. **Who facilitates.** Themselves, a manager, or nobody. If nobody, the course must be self-serve and the facilitator guide becomes a written walkthrough.
6. **Prior artifacts.** Have they run `tech-stack-inventory`, `ai-readiness-survey`, or `prompt-cookbook`? If so, ask for the outputs. A course built on their real stack, their real survey results, and their real recipes is a different product from a generic one.

---

## Step 2: Build the course

Read `references/course-structure.md` and follow it.

Design rules:

- **Start from their real starting point.** If the survey showed 60% already using personal ChatGPT accounts, session one is not "what is AI", it is "here is how to do what you are already doing, safely and better".
- **Every session ends with something they did**, not something they heard. An exercise using their own work, not a toy example.
- **Teach the recipes, not the theory.** If `prompt-cookbook` ran, the course teaches those recipes. Prompting theory is not the goal; getting a specific job done is.
- **Write the facilitator guide for a non-expert.** Include what to say, what will go wrong, and what to do when someone asks a question the facilitator cannot answer. That last one is the most common failure in internal training.
- **Size it honestly.** Three good sessions beat eight that get abandoned after two.

---

## Step 3: Define what success looks like

State up front how they will know the course worked, before they run it.

Not attendance and not satisfaction scores. Something observable: a specific task that used to take a specific amount of time, done differently by a named team, checked at a stated date. One measure is enough; make it real.

Include the honest version of the alternative: if nothing changes eight weeks out, the problem is usually not the course, it is that nobody's job actually requires the new behavior. Say that in the document.

---

## Step 4: Deliver

Write to `~/Documents/<company-slug>-ai-enablement-course.md` and tell them the path.

- Artifact rendering available (claude.ai web, Cowork): emit as a markdown artifact. **Always pass a title.** Cowork rejects the call without one. Use `AI Enablement Course: [Company Name]`.
- Local Claude Code: write to the path above.

This is the last skill in the sequence. Close by naming what to revisit rather than what to run next: the inventory goes stale in a quarter, and the survey is worth repeating once the course has run.

---

## Style and conventions

- **No em dashes.** Use commas, parentheses, or sentence breaks.
- **Plain language.** Employees read the session content, not just the operator.
- **No hype and no inflated outcomes.** Do not promise productivity gains you cannot support. An operator who repeats an invented number to their team loses credibility with the team, not with you.
- **Name what the course will not fix.** Training does not solve a tooling gap, a policy vacuum, or a manager who does not want this.
- Attribution footer: `Created by Blane Warrene, blanewarrene.com`

## When NOT to fire this skill

- A public, sellable course for customers. Use the Teachable Course Builder prompt, which produces an external product.
- Cataloguing tools. Use `tech-stack-inventory`.
- Surveying people. Use `ai-readiness-survey`.
- Building the prompts themselves. Use `prompt-cookbook`.
- Onboarding an acquired team after a deal. That is `people-integration` in Product in Acquisitions OS.
