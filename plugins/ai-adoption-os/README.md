# AI Adoption OS

Four skills that turn AI curiosity into a working plan at a 25 to 150 person company. Built for operators, with product leaders as a secondary reader.

Each skill interviews you first and produces a **completed document**, not a blank template.

| Skill | The operator's question | Produces |
|-------|------------------------|----------|
| `tech-stack-inventory` | What do we run, and where does AI fit? | Populated inventory with overlap, AI you already pay for, and where AI does not belong |
| `ai-readiness-survey` | Where is AI already being used here? | Survey tuned to your roles, plus a rubric for reading the answers |
| `prompt-cookbook` | What do I hand my team on Monday? | Eight to twelve recipes for your vertical, each with a failure mode |
| `enablement-course` | How do I teach this without a consultant? | Session plan, exercises, and a facilitator guide for a non-expert |

They run in that order, but each works standalone. Nothing chains automatically. Each closes by naming the natural next one, once.

## Install

```bash
claude plugin marketplace add enalbenerraw/blanewarrene
claude plugin install ai-adoption-os@blanewarrene-marketplace
```

Run `/reload-plugins` afterward to apply it to a running session.

Works in Claude Code and in Cowork, where document work belongs. In Cowork, install through **Customize** in the desktop sidebar.

## Who this is for

An operator at a company with 25 to 150 employees: a COO, an ops lead, a founder wearing the ops hat, or whoever got handed "figure out AI" alongside their real job. Not technical, busy, and skeptical for good reason.

## What it will not do

- It will not tell you AI is the answer to everything. `tech-stack-inventory` is required to name at least one place AI does not belong.
- It will not invent productivity statistics. Every number is labeled published, reported, or estimated, and the three are never blended.
- It will not promise training fixes a tooling gap, a policy vacuum, or a manager who does not want this. `enablement-course` names those up front.

## Relationship to the Word documents

The four `.docx` files in [`prompts/ai-smb-toolkit/`](../../prompts/ai-smb-toolkit/) remain available and maintained. They are blank templates you fill in yourself, they need no AI tool at all, and they serve people who will never open a Claude surface.

These skills are the other half: same four jobs, but they do the first pass for you. Pick whichever fits where you work.

## Not to be confused with

- **Teachable Course Builder** (in `prompts/`) builds a public, sellable course for your customers. `enablement-course` builds internal training for your own staff.
- **Market Intelligence** researches other companies. This plugin is about the company you work at.
- **Product in Acquisitions OS** covers post-acquisition integration, including acquired-team onboarding, which is a different situation with different stakes.

## License

MIT. See [`LICENSE`](LICENSE).

## Author

Blane Warrene. [blanewarrene.com](https://blanewarrene.com)
