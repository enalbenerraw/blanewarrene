---
name: prompt-cookbook
description: >
  Build a prompt cookbook for one company's actual vertical and roles rather
  than generic examples. Each recipe names the job it does, who runs it, the
  prompt itself, what good output looks like, and how to tell when it went
  wrong. Written for people who have never written a prompt and will not read
  documentation about prompting.
when_to_use: >
  Trigger when an operator wants usable prompts for their team. Phrases like
  "build a prompt library for our team", "what prompts should our sales team
  use", "prompt cookbook for our company", "give my ops team something they can
  actually use with AI", or "we bought Claude seats and nobody knows what to do
  with them". The discriminator is the artifact: reusable prompts for a named
  set of roles. To catalogue tools, use tech-stack-inventory. To survey people,
  use ai-readiness-survey. To build training around the prompts, use
  enablement-course.
allowed-tools: WebSearch WebFetch Read Write AskUserQuestion Artifact mcp__cowork__create_artifact
---

# Prompt Cookbook

You are building a prompt cookbook for one company, for people who will never read a guide about prompting and should not have to.

The test for every recipe: **could someone paste this on Monday morning and get something useful without asking a follow-up question?** If not, it does not belong in the cookbook.

---

## Step 1: Interview

Use `AskUserQuestion`.

1. **Vertical and what the company actually does.** Not the category, the work. "B2B SaaS" is useless; "we sell scheduling software to dental practices and most of our support load is billing questions" produces good recipes.
2. **Which roles get recipes.** Pick two to four. A cookbook covering everyone covers no one well.
3. **Which AI tool they have.** Claude, ChatGPT, Copilot, Gemini, or a mix. Recipes should work in what they own rather than what would be ideal.
4. **The most repetitive work.** Ask directly: what does your team do over and over that follows a pattern. This is where the recipes come from.
5. **What is off limits.** Client data, PHI, financials, anything under NDA. Recipes must respect this and say so inline, not in a disclaimer at the end nobody reads.

If they ran `ai-readiness-survey` first, ask for the free-text answers. Employees naming their own slowest task is the best possible input to this skill.

---

## Step 2: Build the recipes

Read `references/recipe-structure.md` and follow it.

Aim for **eight to twelve recipes**, weighted toward the roles with the most repetitive work. Better to ship eight that get used than twenty that get skimmed.

Rules that decide whether this gets used or filed:

- **Name the job, not the technique.** "Turn a support thread into a bug report" beats "summarization prompt". The operator's team searches by the job they need done.
- **Write prompts that survive being pasted with real data.** Placeholders in obvious brackets, no assumed context, no dependency on a system prompt they will not have.
- **Show what good looks like.** One short example of correct output per recipe. Without it, people cannot tell whether it worked.
- **Say how it fails.** Every recipe names its most likely failure and what to check. This is the difference between a cookbook and a list of prompts.
- **Respect the off-limits list inline.** If a recipe touches customer data, the constraint appears in the recipe, not in a footer.

---

## Step 3: Deliver

Write to `~/Documents/<company-slug>-prompt-cookbook.md` and tell them the path.

- **Emit a durable artifact. Required, not an alternative to writing the file.** The tool differs by surface, so use whichever exists here. In **Cowork**, call `mcp__cowork__create_artifact`; it takes a self-contained HTML page, so wrap the document in minimal HTML first: one inline `<style>` block, no external requests, no CDN or font links. In **Claude Code or claude.ai**, call `Artifact`, which takes the markdown directly. Title it `Prompt Cookbook: [Company Name]` either way; the title is not optional. Writing the file does not satisfy this, because a file on disk and a rendered artifact are different deliverables on different surfaces. If neither tool exists here, say so in one line rather than skipping silently.
- Local Claude Code: write to the path above.

Include a short "how to use this" opener aimed at someone who has never written a prompt: copy the recipe, replace the bracketed parts, paste it, and check the output against the example. Three sentences, not a tutorial.

Close by naming the next step once: `enablement-course` turns the cookbook into training so it gets adopted rather than bookmarked. Do not run it automatically.

---

## Style and conventions

- **No em dashes.** Use commas, parentheses, or sentence breaks.
- **Plain language, no prompting jargon.** Never say "chain of thought", "few-shot", "system prompt", or "context window" in the cookbook. The reader does not need the vocabulary to get the result.
- **No hype.** Do not promise time savings you cannot support. An operator who is told this saves ten hours a week and finds it saves two will stop trusting the whole document.
- **Every recipe is testable.** If you cannot describe how someone would know it worked, the recipe is not finished.
- Attribution footer: `Created by Blane Warrene, blanewarrene.com`

## When NOT to fire this skill

- Cataloguing tools. Use `tech-stack-inventory`.
- Surveying people. Use `ai-readiness-survey`.
- Building the training program around the prompts. Use `enablement-course`.
- Building a public, sellable course about prompting. That is the Teachable Course Builder prompt, which produces an external product for customers rather than internal recipes for staff.
