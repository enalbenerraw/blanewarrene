# Four-Agent Fleet

Four subagents with hard role boundaries, plus a routing skill that tells the main agent when to delegate and what it keeps for itself. Discovery and execution run on cheaper models at lower effort, judgment runs on Opus, and every agent returns a length-capped report so the main session does not pay to re-read long answers.

| Agent | Model | Job | Can change files? |
|-------|-------|-----|-------------------|
| `explorer` | Haiku, low effort | Finds where things live and returns `path:line` plus a short summary | No |
| `implementer` | Sonnet, medium effort | Makes a change whose approach is already decided, then verifies it | Yes, never commits or deploys on its own |
| `reviewer` | Opus, high effort | Plans non-trivial changes before work starts, reviews diffs and drafts after | No |
| `researcher` | Sonnet, medium effort | Sourced web research and read-only Notion lookups | No, never writes to Notion |

The `fleet-routing` skill runs the standard sequence for non-trivial work: explorer locates, reviewer plans, implementer builds, reviewer checks, and the main agent reports. It also defines what never leaves the main agent: synthesis, user communication, commits, deploys, and Notion writes.

## Where this came from

This plugin packages two ideas:

- **The four-agent system I run in Claude Code**, written up in [A Four-Agent Starter Fleet for Claude Code (with a Notion brain)](https://blanewarrene.com/2026/06/24/a-four-agent-starter-fleet-for-claude-code/) (June 24, 2026). The plugin turns those personal agent files into something anyone can install, including Claude Desktop users who never touch a terminal.
- **Cost awareness, prompted by Uday Kamath's** [From $19 to $0.16: A Step-by-Step Guide to Cutting the Cost of LLM Inference](https://udaykamath.substack.com/p/from-19-to-016-a-step-by-step-guide) (November 21, 2026). His guide works at the GPU serving layer. Its discipline carries over: measure cost per unit of work, keep the stable prefix stable so it caches, and spend the expensive tier only where it earns its keep.

## How the fleet keeps cost down

Claude Code and Cowork make the API calls, so caching, Batch, and `max_tokens` are theirs to manage. The plugin controls the levers that remain:

| Lever | What the plugin does |
|-------|---------------------|
| Model routing | Discovery on Haiku, execution and research on Sonnet, judgment pinned to Opus so it never silently inherits a pricier or weaker session model |
| Effort | `low` for the explorer, `medium` for the implementer and researcher, `high` only for the reviewer |
| Output control | Every report is length-capped (150 to 300 words, or 7 ranked findings), because each report is re-read at the main session's input rate |
| Cache-friendly prompts | Agent prompts are static, with no dates or per-run values, and the routing skill continues a finished agent instead of starting a cold one |

**By the numbers (Claude API list prices per million tokens, November 2026):**

| Model | Input | Output |
|-------|-------|--------|
| Claude Haiku 5.5 | $0.10 | $0.50 |
| Claude Sonnet 5.5 | $2.00 | $10.00 |
| Claude Opus 5.5 | $4.00 | $20.00 |

On a subscription plan you pay in usage limits rather than dollars, and the same routing stretches them the same way.

## Install

```bash
claude plugin marketplace add enalbenerraw/blanewarrene
claude plugin install four-agent-fleet@blanewarrene-marketplace
```

Run `/reload-plugins` afterward to apply it to a running session.

### Claude Desktop

1. Download `four-agent-fleet.plugin` from the [latest release](https://github.com/enalbenerraw/blanewarrene/releases/tag/fleet-v0.1.0).
2. In the Claude Desktop app, open **Cowork**, then **Customize** in the sidebar.
3. Drop in the `.plugin` file and confirm.
4. Ask "which subagents do you have?" to confirm all four loaded.

Subagents run in Cowork and Claude Code. Plain chat has no subagents, so the fleet does not apply there.

## Who this is for

An operator or product leader who runs real work through Claude and wants delegation to be predictable: the same four roles, the same boundaries, on every surface.

## Known limits

- **Model routing depends on the surface.** Claude Code honors each agent's `model` setting. If a surface ignores it, agents run on the session model, which still works but costs more. The `effort` setting follows the same rule.
- **Notion access depends on the connector.** The researcher lists the claude.ai Notion connector's read-only tools. If your Notion connection exposes different tool names, the researcher says so and answers from the web only. It never gains write access.
- **Explorer and reviewer keep Bash** for read-only inspection like `git log` and running tests. Their read-only rule is enforced by instruction, not by the tool list.

Created by Blane Warrene, blanewarrene.com
