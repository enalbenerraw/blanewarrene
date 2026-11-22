---
name: fleet-routing
description: >
  Route work across the four-agent fleet (explorer, implementer, reviewer,
  researcher): decide what to delegate, to which agent, and what the main
  agent keeps. Applies to any multi-step task that involves finding things,
  changing files, reviewing a plan or diff, or researching outside facts or a
  Notion knowledge base.
when_to_use: >
  Trigger at the start of any task with three or more steps, any change to
  code or files, any plan or diff that needs review, and any question that
  needs web or Notion research. Also trigger when the user says "use the
  fleet", "delegate this", "have the reviewer check", "send the researcher",
  or names any of the four agents.
---

# Fleet routing

Delegate to the four fleet agents without waiting to be asked when a task fits. Keep coordination with the main agent.

## Pick the agent

| Need | Agent | Model |
|------|-------|-------|
| Find where something lives, map a folder or codebase | `explorer` | Haiku, low effort |
| Make a change whose approach is already decided | `implementer` | Sonnet, medium effort |
| Plan a non-trivial change, or review a diff or draft | `reviewer` | Opus, high effort |
| Outside facts, sourced answers, Notion lookups | `researcher` | Sonnet, medium effort |

## Run the standard sequence for non-trivial changes

1. Send `explorer` to locate the relevant files.
2. Send `reviewer` to plan the change. Show the plan to the user before code changes if they have not seen it.
3. Send `implementer` to make the change and verify it.
4. Send `reviewer` to review the result adversarially.
5. Report to the user what changed, where, and how it was verified.

Send `researcher` at any step that needs outside facts or a past decision.

## Delegate only when it pays

- Delegate when the task is concrete, bounded, and can run on its own.
- Do it directly when coordination would cost more than the work: a single file read, a one-line edit, a question you can already answer.
- One agent per bounded task. No fan-out swarms.
- Continue a finished agent with a follow-up message instead of starting a fresh one on the same thread of work.

## Keep these with the main agent

- Synthesis across agent reports, and every message to the user. Agent reports are not visible to the user, so relay what matters.
- Authorization decisions, commits, pushes, deploys, and anything sent outside the session.
- All Notion writes. Reconcile against current page content before writing.

## Hold the role boundaries

- `explorer`, `reviewer`, and `researcher` never change files or external systems.
- `researcher` never writes to Notion.
- `implementer` never commits, pushes, or deploys unless the task explicitly says to.
