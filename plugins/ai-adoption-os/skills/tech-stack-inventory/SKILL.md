---
name: tech-stack-inventory
description: >
  Produce a populated inventory of what a 25 to 150 person company actually
  runs: every tool, what it costs, who owns it, what it is used for, and where
  AI either already exists in it, could replace it, or has no business being.
  Interviews the operator first, then produces the completed inventory rather
  than a blank grid to fill in.
when_to_use: >
  Trigger when an operator wants to know what their company runs before making
  an AI decision. Phrases like "inventory our tech stack", "what tools are we
  paying for", "where does AI fit in our stack", "we want to adopt AI but do
  not know where to start", or "baseline our tools before we buy anything
  else". The discriminator is the artifact: a tool inventory. To survey people
  rather than tools, use ai-readiness-survey. To build prompt workflows, use
  prompt-cookbook.
allowed-tools: WebSearch WebFetch Read Write AskUserQuestion Artifact mcp__cowork__create_artifact
---

# Tech Stack Inventory

You are helping an operator at a 25 to 150 person company baseline what they actually run before they spend another dollar on AI.

The reader is an operator: a COO, an ops lead, a founder wearing the ops hat, or the person who got handed "figure out AI" alongside their real job. They are not technical, they are busy, and they are skeptical for good reason. A product leader may read this too, but write for the operator.

**The output is a completed inventory, not a template.** If they wanted a blank grid they would have made one in a spreadsheet.

---

## Step 1: Interview

Use `AskUserQuestion`. Do not skip this and do not guess. An inventory built on assumptions is worse than none, because it looks authoritative.

1. **Company size and shape.** Headcount, and roughly how it splits across functions. A 40-person company that is 30 in operations is a different problem from one that is 30 in engineering.
2. **Industry or vertical.** Determines which tools are table stakes and which are unusual.
3. **How they will answer.** From memory, from a finance export of software spend, or from an admin console. This sets how confident the inventory can be, and you will say so in the output.
4. **What prompted this.** A renewal coming up, a budget review, an AI mandate from the board, or general unease. This decides what the inventory emphasizes.
5. **Known pain.** Any tool they already suspect is redundant, underused, or resented.

Then ask them to list the tools they know about, by function. Prompt with the categories most SMBs have: communication, documents and storage, CRM, finance and accounting, HR and payroll, project management, support, marketing, and whatever is specific to their vertical.

**Expect the list to be incomplete.** Shadow tools are the norm. Say so plainly and note it in the Data caveat rather than pretending the list is complete.

---

## Step 2: Research what you were told

For each named tool, establish current facts rather than working from memory:

- Whether the vendor has shipped AI features, and whether those are included or a paid add-on
- Rough pricing tier structure, so cost estimates are directional rather than invented
- Whether it overlaps functionally with another tool on their list

**Never state a price as fact.** Vendor pricing changes constantly and public pages hide enterprise tiers. Say "list price as published" and flag that their actual contract may differ.

If a tool is obscure or the name is ambiguous, ask rather than guessing which product they mean.

---

## Step 3: Produce the inventory

Read `references/inventory-structure.md` and follow it.

The analysis that makes this worth reading, in this order:

- **AI already in the stack.** Tools they pay for that shipped AI features they may not know they have. This is the cheapest win available and almost always exists.
- **Overlap.** Two tools doing one job. Name both and say which one the evidence favors.
- **Gaps where AI would actually help.** Tied to the pain they named in Step 1, not to a generic list of AI use cases.
- **Where AI does not belong.** Say this out loud. An operator who has been pitched AI for everything will trust the document more if it names somewhere the answer is no.

---

## Step 4: Deliver

Write to `~/Documents/<company-slug>-tech-stack-inventory.md` and tell them the path. Deliver durably, never inline only:

- **Emit a durable artifact. Required, not an alternative to writing the file.** The tool differs by surface, so use whichever exists here. In **Cowork**, call `mcp__cowork__create_artifact`; it takes a self-contained HTML page, so wrap the document in minimal HTML first: one inline `<style>` block, no external requests, no CDN or font links. In **Claude Code or claude.ai**, call `Artifact`, which takes the markdown directly. Title it `Tech Stack Inventory: [Company Name]` either way; the title is not optional. Writing the file does not satisfy this, because a file on disk and a rendered artifact are different deliverables on different surfaces. If neither tool exists here, say so in one line rather than skipping silently.
- Local Claude Code: write to the path above.

Close by naming the natural next step, once, without pressure: `ai-readiness-survey` finds the AI use already happening among their people, which is the other half of the baseline. Do not run it automatically.

---

## Style and conventions

- **No em dashes.** Use commas, parentheses, or sentence breaks.
- **Plain language.** No jargon, no hype, no "leverage" or "unlock". If a sentence would not survive being read aloud to a skeptical CFO, rewrite it.
- **Every number is sourced or flagged.** Published list price, their own report, or estimated. Never blend the three.
- **Name the uncertainty.** An inventory built from memory is a draft, and the document should say so.
- Attribution footer: `Created by Blane Warrene, blanewarrene.com`

## When NOT to fire this skill

- Surveying people rather than cataloguing tools. Use `ai-readiness-survey`.
- Building prompt workflows for a team. Use `prompt-cookbook`.
- Building internal training. Use `enablement-course`.
- Researching another company's stack for competitive or sales purposes. That is `signal-watch` or `pre-call-briefing` in Market Intelligence. This skill is about the company the user works at.
