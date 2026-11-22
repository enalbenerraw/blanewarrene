# Four-Agent Fleet

Four subagents with hard role boundaries, plus a routing skill that tells the main agent when to delegate and what it keeps for itself. Discovery and execution run on cheaper models at lower effort, judgment runs on Opus, and every agent returns a length-capped report so the main session does not pay to re-read long answers.

| Agent | Model | Job | Can change files? |
|-------|-------|-----|-------------------|
| `explorer` | Haiku, low effort | Finds where things live and returns `path:line` plus a short summary | No |
| `implementer` | Sonnet, medium effort | Makes a change whose approach is already decided, then verifies it | Yes, never commits or deploys on its own |
| `reviewer` | Opus, high effort | Plans non-trivial changes before work starts, reviews diffs and drafts after | No |
| `researcher` | Sonnet, medium effort | Sourced web research and read-only Notion lookups | No, never writes to Notion |

The `fleet-routing` skill runs the standard sequence for non-trivial work: explorer locates, reviewer plans, implementer builds, reviewer checks, and the main agent reports. It also defines what never leaves the main agent: synthesis, user communication, commits, deploys, and Notion writes.

## Install

```bash
claude plugin marketplace add enalbenerraw/blanewarrene
claude plugin install four-agent-fleet@blanewarrene-marketplace
```

Run `/reload-plugins` afterward to apply it to a running session.

Works in Claude Code and in Cowork. In Cowork, install through **Customize** in the desktop sidebar, or drop in the `.plugin` file from the latest release.

## Who this is for

An operator or product leader who runs real work through Claude and wants delegation to be predictable: the same four roles, the same boundaries, on every surface.

## Known limits

- **Model routing depends on the surface.** Claude Code honors each agent's `model` setting. If a surface ignores it, agents run on the session model, which still works but costs more. The `effort` setting follows the same rule.
- **Notion access depends on the connector.** The researcher lists the claude.ai Notion connector's read-only tools. If your Notion connection exposes different tool names, the researcher says so and answers from the web only. It never gains write access.
- **Explorer and reviewer keep Bash** for read-only inspection like `git log` and running tests. Their read-only rule is enforced by instruction, not by the tool list.

Created by Blane Warrene, blanewarrene.com
