# Agent instructions

This repo's working context lives in [CLAUDE.md](CLAUDE.md). Read it before making changes. It is the source of truth for repo layout, the release process, and author conventions, and it applies to every agent working here, not just Claude Code.

Keeping the detail in one file is deliberate. A second copy of it drifts.

## Non-negotiables

- **No em dashes anywhere.** Use commas, parentheses, or sentence breaks.
- **CxO tone.** Direct, evidence-led, peer to peer, never sycophantic.
- **Do not modify `SKILL.md` files** unless explicitly asked. They are hand-tuned for tone and trigger phrasing.
- **Do not regenerate reference templates** under `plugins/*/skills/*/references/`. Those are the source of truth.

## Naming, whatever agent you are

The artifacts in `plugins/` are Claude Code plugins. That is a fact about what they are, not about which agent is reading this file. So the paths and commands do not change based on your runtime:

- Plugin manifests live at `plugins/<name>/.claude-plugin/plugin.json`.
- The marketplace manifest is `.claude-plugin/marketplace.json` at the repo root.
- The CLI is `claude plugin install`, `claude plugin tag`, and so on.

Do not rewrite these to match your own product name. A previous version of this file did exactly that and documented directories and commands that do not exist.

## Before you commit

Run the pre-flight checks in [CLAUDE.md](CLAUDE.md) under "Working conventions" against any plugin you touched. The release workflows run the same checks, so catching a failure locally avoids a broken tag push.
