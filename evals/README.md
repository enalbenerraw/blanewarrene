# Researcher regression harness

Regression tests for the three research subagents that ship in this repo's plugins. Each spawns a real subagent against a fixed target with documented ground truth and asserts on the returned dossier.

```bash
./evals/run.sh --list                                # case ids and cost
./evals/run.sh                                       # every case
./evals/run.sh entity-researcher-phantom-round       # one case
```

Exit 0 if everything passed, 1 if any case failed, 2 on a setup problem. Requires `claude` and `jq`.

## Why this exists

`claude plugin eval` is the right tool for this and is gated behind early access as of Claude Code 2.1.223. It refuses on every target including Anthropic's own plugins, is absent from the published docs, and has no documented enrollment path.

Rather than wait, this harness covers the same ground in a degraded form. It is worse than `plugin eval` in specific ways: no scoring, no baseline arm, no ablation, no judge model, and pattern matching instead of graded rubrics. It is much better than the alternative, which was no regression coverage at all on two published plugins whose behavior changed in `0.4.0`.

## What each case asserts

| Field | Meaning |
|---|---|
| `required_patterns` | Must all be present. Section headings, verification labeling. |
| `forbidden_patterns` | Must all be absent. Regressions with a known signature, such as the hardcoded `### 90-day messaging themes` heading fixed in `clb-v0.4.0`. |
| `must_flag` | A documented fabrication that must appear somewhere in the dossier, meaning the agent surfaced and labeled it rather than silently carrying it as fact. |

`must_flag` is the interesting one and the reason this harness is worth running. Its patterns are deliberately loose. It cannot distinguish "correctly flagged as fabricated" from "repeated as fact," so it proves the agent *engaged with* the claim, not that it reached the right conclusion. Read the dossier in `results/` when a `must_flag` case passes. That is a real limitation, not a rough edge to paper over.

## Ground truth

The fabrications the cases hunt for are real and were caught during verification on 2026-08-06 and 2026-08-07:

- **`techstackipo.com`** publishes "Notion S-1 Filed: $18.5B, IPO In Progress 2026". No such registration statement exists on EDGAR and no credible outlet reports one.
- **`salestools.io`** publishes a Linear "Series D, $50M at $650M valuation". It is priced *below* the documented $82M Series C at $1.25B post from June 2025, and no credible source carries it. Two independent researcher instances caught it separately, blind.

Both would have entered a brief as fact under the pre-`0.4.0` agents, which contained zero verification instructions.

These fixtures decay. If an aggregator corrects a page or drops it, the corresponding `must_flag` will start failing for a reason that has nothing to do with the agent. When that happens, replace the fixture rather than deleting the assertion, and update `ground_truth` in the case file.

## Cost

Every case spawns a real subagent that makes real web searches. Budget roughly 3 to 5 minutes and about 20 searches per case. This is not a test suite to run on every commit. Run it when a researcher agent or its calling skill changes.

## Migration to `claude plugin eval`

When early access opens, the case files translate directly. The documented layout is `evals/**/case.yaml` or `evals/**/prompt.md` plus `graders/*.md`. Each case here maps to:

- `prompt` becomes the case prompt
- `required_patterns` and `forbidden_patterns` become deterministic graders
- `must_flag` becomes an LLM grader, which is where the real gain is: a judge model can tell "correctly identified as fabricated" from "repeated as fact," which grep cannot
- `ground_truth` becomes the grader rubric

Keep `run.sh` until the migration is verified, then delete this directory.

## Adding a case

Drop a JSON file in `cases/`. The runner is generic and discovers whatever is there. Copy an existing file for the shape. Every case needs an honest `ground_truth` explaining why the assertion is correct, and a `cost_note` so nobody runs it by accident.
