# Contributing

Thanks for considering a contribution. This prompt exists because real GTM and executive workflows benefit from a shared, improvable briefing playbook. Every real-world usage pattern is a potential contribution.

## How to contribute

### Small improvements

Open a pull request directly. Examples of small improvements:

- Tightening a phrase that produces inconsistent output.
- Adding a source type to the research protocol (for example, a government procurement database that is useful for a specific vertical).
- Fixing a formatting rule that breaks on certain Claude surfaces.
- Clarifying a clarifying question.

### Larger changes

Open an issue first and describe the proposed change. Examples of larger changes:

- Adding a new output format (for example, a PowerPoint deck variant).
- Adding a new use-case path (for example, M&A screening).
- Restructuring the research protocol.
- Adding automation scaffolding (for example, a wrapper script that runs the prompt in batch).

## Evaluation criteria

A change is worth merging if it makes the briefing more decision-useful for a real GTM conversation. That is the only bar.

Concretely, the maintainer evaluates proposed changes against four questions:

1. Does the change preserve the four design principles stated in the README? (Clarifying questions up front, synthesis over research dumps, structured source protocol, provocation at the end.)
2. Does the change produce at least one non-obvious insight the reader would not have surfaced on their own?
3. Does the change work across multiple Claude surfaces (web, Code, Cowork, API) or does it constrain the prompt to one surface?
4. Does the change add length without adding value? Brevity is a feature.

## Writing style for prompt text

If you edit the prompt itself:

- Avoid em dashes. Use commas, colons, or sentence breaks instead.
- Write in direct, declarative sentences. No filler, no throat-clearing.
- Name the specific action Claude should take, not the desired feeling. "Produce a three-column table" is better than "make it look professional."
- When you add instructions, add examples. The prompt is a specification, not a vision statement.

## Writing style for documentation

- README and CONTRIBUTING are written in the same voice as the prompt: direct, evidence-led, no filler.
- Tables are welcome for comparisons and reference material.
- Code blocks are welcome for directory structures and example commands.

## Testing changes

Before submitting a pull request, run the modified prompt against at least three real target companies representing different profiles:

1. A large, public incumbent with rich public data.
2. A mid-market private company with moderate public footprint.
3. An early-stage startup with thin public data.

The prompt must produce useful output for all three. If it breaks on the thin-data case, either improve the fallback behavior or note the limitation in the README.

## Commit messages and PR descriptions

- Keep commit messages action-oriented: "Add procurement-database source to research protocol," not "Update prompt."
- PR descriptions should answer three questions: what changed, why, and what was tested.

## Code of conduct

Be direct, be kind, be specific. Disagreements about prompt design are welcome; ad hominem is not.

## License

By contributing, you agree that your contributions will be licensed under the MIT license that covers this repository.
