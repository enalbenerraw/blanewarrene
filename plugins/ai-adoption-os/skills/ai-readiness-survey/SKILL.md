---
name: ai-readiness-survey
description: >
  Generate an employee survey tuned to a company's size, vertical, and role mix,
  designed to surface the AI use already happening informally rather than to
  measure enthusiasm. Produces the questions, the distribution plan, the
  anonymity commitment, and a rubric for reading the results, including which
  answers mean act now and which mean do nothing.
when_to_use: >
  Trigger when an operator wants to know how their people are actually using AI.
  Phrases like "survey our team about AI", "find out who is already using
  ChatGPT here", "AI readiness assessment", "we need to know where AI is being
  used before we set a policy", or "shadow AI audit". The discriminator is the
  artifact: a survey aimed at people. To catalogue tools instead, use
  tech-stack-inventory. To build workflows for a team, use prompt-cookbook.
allowed-tools: WebSearch WebFetch Read Write AskUserQuestion Artifact
---

# AI Readiness Survey

You are helping an operator find out how their people already use AI, so policy and training are built on evidence instead of assumption.

**The survey's job is discovery, not enthusiasm measurement.** Most AI surveys ask "how excited are you about AI" and produce numbers nobody can act on. This one is built to surface what is already happening in the shadows, because at a 25 to 150 person company it is always already happening.

---

## Step 1: Interview

Use `AskUserQuestion`.

1. **Headcount and role mix.** Sales, ops, finance, support, engineering, marketing, and roughly how many in each. Questions differ by function.
2. **Vertical.** Determines which regulatory or client-confidentiality constraints belong in the framing.
3. **Current AI policy.** None, an informal norm, a written policy, or a ban. **A ban changes everything**, because a survey run under a ban collects lies unless anonymity is credible and stated.
4. **Who sends it.** The founder, an ops lead, or HR. Changes the tone and the honest-answer rate.
5. **What they will do with the results.** Set policy, budget training, pick a platform, or decide whether to act at all. Say this in the survey preamble, because employees answer differently when they know.

---

## Step 2: Build the survey

Read `references/survey-structure.md` and follow it.

Design rules that matter more than the question list:

- **Ask about behavior, not attitude.** "Which tools have you used for work in the last month" beats "how do you feel about AI". Behavior is actionable; sentiment is not.
- **Make admitting unsanctioned use safe.** If the honest answer could get someone in trouble, you will not get it. State the anonymity commitment in plain words and mean it.
- **Keep it under ten questions.** Completion rate collapses past that, and a survey half the company ignores tells you about the half that answered.
- **Include one free-text question**, the one that reliably produces the most useful answer: what task takes you the longest that you suspect a machine could help with.
- **Tune by function.** A support rep and a controller have different plausible AI tasks. Generic questions produce generic answers.

---

## Step 3: Write the reading rubric

This is the part most surveys skip and the reason most survey results go unused.

For each question, state in advance what a given answer means and what to do about it. For example: if more than a third report using a personal AI account for work, the finding is not "our people are enthusiastic," it is "we have an unmanaged data exposure and a training gap, in that order."

Name at least one result pattern that should lead to **doing nothing**. An operator who only ever gets recommendations to act will discount all of them.

---

## Step 4: Deliver

Write to `~/Documents/<company-slug>-ai-readiness-survey.md` and tell them the path.

- Artifact rendering available (claude.ai web, Cowork): emit as a markdown artifact. **Always pass a title.** Cowork rejects the call without one. Use `AI Readiness Survey: [Company Name]`.
- Local Claude Code: write to the path above.

Include the distribution plan: which tool to send it in, what the intro message says, how long to leave it open, and what to tell people about what happens next.

Close by naming the next step once: `prompt-cookbook` turns what the survey finds into workflows people can use. Do not run it automatically.

---

## Style and conventions

- **No em dashes.** Use commas, parentheses, or sentence breaks.
- **Plain language.** Employees will read this, not just the operator who commissioned it.
- **Never promise anonymity the tooling cannot deliver.** If they plan to send it through a tool that records respondent identity, say so and adjust the wording rather than making a promise that will be broken.
- **Do not invent benchmark statistics.** "Most companies see X% adoption" is the kind of claim that gets repeated in a board meeting and cannot be defended. If a benchmark is cited, source it or drop it.
- Attribution footer: `Created by Blane Warrene, blanewarrene.com`

## When NOT to fire this skill

- Cataloguing tools rather than surveying people. Use `tech-stack-inventory`.
- Building prompt workflows. Use `prompt-cookbook`.
- Building internal training. Use `enablement-course`.
- Post-acquisition employee retention and belonging. That is `people-integration` in Product in Acquisitions OS, which is a different situation with different stakes.
