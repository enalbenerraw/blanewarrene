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

`must_flag` is the interesting one and the reason this harness is worth running. It is also the one that needed a design correction after the first real run.

**Supply the unreliable claim in the prompt. Do not hope the agent finds it.** The first version of `entity-researcher-phantom-round` asserted that a fabricated funding round would appear in the dossier, on the theory that the agent would encounter the aggregator page during research. It did, twice. Then a third run never hit the page, produced a perfectly good 41-line dossier in 127s against a 195-line one earlier, and failed the assertion. Nothing had regressed. The test was measuring search coverage, which varies run to run, rather than verification behavior, which is the capability under test.

The fix is to hand the claim to the agent as unverified background and assert on what it does with it. That is deterministic and tests the right thing.

Even so, the patterns stay loose. The `phantom round rejected` assertion requires a rejection word in the same sentence as the claim, which is stronger than mere co-occurrence but still not proof the agent reasoned correctly. Read the dossier in `results/` when a `must_flag` case passes. This is the specific weakness a judge model fixes, and the main reason migrating to `claude plugin eval` is still worth doing.

## Ground truth

The fabrications the cases hunt for are real and were caught during verification on 2026-08-06 and 2026-08-07:

- **`techstackipo.com`** publishes "Notion S-1 Filed: $18.5B, IPO In Progress 2026". No such registration statement exists on EDGAR and no credible outlet reports one.
- **`salestools.io`** publishes a Linear "Series D, $50M at $650M valuation". It is priced *below* the documented $82M Series C at $1.25B post from June 2025, and no credible source carries it. Two independent researcher instances caught it separately, blind.

Both would have entered a brief as fact under the pre-`0.4.0` agents, which contained zero verification instructions.

These fixtures decay. If an aggregator corrects a page or drops it, the corresponding `must_flag` will start failing for a reason that has nothing to do with the agent. When that happens, replace the fixture rather than deleting the assertion, and update `ground_truth` in the case file. Supplying the claim in the prompt makes the case robust to the page disappearing, since the agent is asked to evaluate the claim rather than to find it, but a corrected underlying fact would still invalidate the assertion.

## Running it

Do not pipe the runner through `tee`. The pipeline returns `tee`'s exit status, so a failing run reports success. Redirect instead:

```bash
./evals/run.sh > run.log 2>&1; echo "exit=$?"
```

## What this harness cannot test

**Artifact emission.** The runner executes through `claude -p`, and headless CLI
sessions have no artifact tool. Confirmed on 2026-08-07 by direct probe and by a
skill run that searched for it and found nothing. Cowork exposes
`mcp__cowork__create_artifact`; claude.ai and interactive Claude Code expose
`Artifact`. None of them are reachable from here.

That matters because artifact emission is where a real bug shipped: on
2026-08-07 `tech-stack-inventory` wrote correct markdown in Cowork and produced
no artifact, because delivery was worded as an optional menu item and named a
tool that does not exist in Cowork. **Verifying that fix requires a manual run in
Cowork.** There is no automated substitute.

An attempt to guard the fallback branch instead (the skill must announce a
missing artifact tool rather than skip silently) was written and dropped. The
skill behaves correctly, but the only observable evidence is free-form prose,
and three regex assertions against it failed for three different reasons while
the product was fine. Prose matching is not a reliable instrument, which is the
same lesson `must_flag` taught. Tool-call assertions are reliable; text
assertions against chat commentary are not.

## Case modes

| `mode` | What it runs | What it asserts on |
|--------|--------------|--------------------|
| `subagent` (default) | Spawns one subagent via the Task tool | The returned dossier text |
| `skill` | Invokes a named skill via the Skill tool | Response text, plus `required_tools` against the tool calls actually made |

`required_tools` is the reliable half. It reads the `tool_use` names out of the
`stream-json` output, so it catches "the skill never called the tool at all",
which no text assertion can see. Prefer it over text matching wherever the
behavior under test is a call rather than a phrase.

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
