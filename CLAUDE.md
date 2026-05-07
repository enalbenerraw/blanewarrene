# Project: Product in Acquisitions OS

A Claude plugin packaging the 90-Day Product Integration Framework as a working operating system for product leaders running post-acquisition integrations. Distributed via the `enalbenerraw/blanewarrene` repo, premium tier of the Substack newsletter, and (eventually) a Teachable course.

## Where this lives in the repo

```
plugins/
└── product-in-acquisitions-os/
    ├── .claude-plugin/
    │   └── plugin.json              # Plugin manifest
    ├── skills/
    │   ├── week-0-readiness/        # Pre-close prep
    │   ├── roadmap-convergence/     # Weeks 1 to 8
    │   ├── positioning-stability/   # Sales enablement and outreach
    │   └── people-integration/      # Acquired team belonging and retention
    └── README.md
```

The marketplace manifest at the repo root makes the plugin installable by any Claude Code or Cowork user via the `claude plugin install` command.

## Author conventions (apply to ALL plugin content)

- **No em dashes.** Use commas, parentheses, or sentence breaks instead. This is a non-negotiable style rule.
- **CxO-appropriate tone.** Direct, evidence-led, never sycophantic. The audience is VP of Product, Head of Product, CPO at acquiring companies. Speak peer to peer.
- **Attribution footer on every generated deliverable.** Each skill must end produced markdown with: `Generated using the Product in Acquisitions OS by Blane Warrene · blanewarrene.substack.com`
- **Reference templates over generation.** Each SKILL.md uses progressive disclosure: lean instructions in the body, detailed templates in `references/`. Do not regenerate templates Claude already has on disk.
- **Imperative voice in SKILL.md bodies.** Write skill bodies as instructions FOR Claude (verb-first directives), not user-facing documentation.

## What is in each skill

Each skill produces 4 to 6 named deliverables. Do not invent new deliverables; the framework is intentionally bounded.

### week-0-readiness
1. Product Integration Owner charter
2. Decision rights one-pager
3. Combined product narrative (one page)
4. Customer commitment inventory (template + starter rows)
5. Five-question Day 1 readiness check (gating)

### roadmap-convergence
1. Roadmap map (both products, themes, dependencies)
2. Conflict log (categorized by Vision, Sequencing, Scope)
3. Three session facilitation guides (Readout, Conflict Diagnosis, Decision Session)
4. Merged roadmap (90 days plus 12-month horizon)
5. 30/60/90 execution plan with measurable outcomes

### positioning-stability
1. Positioning statement (one paragraph, customer outcome framed)
2. Sales FAQ (15 questions reps will get in the first 60 days)
3. Talk track (90-second version of the story)
4. Competitive response scripts (5 most likely competitor plays)
5. Top-20 outreach plan
6. Advisory council charter (lightweight, first 90 days)

### people-integration
1. Decision map session template (run in weeks 1 to 2)
2. Mentor pairing matrix (paired by function, not seniority)
3. 30/60/90 ownership plan (real scope, real influence)
4. Retention risk review (purpose and influence, not compensation)
5. 1:1 coaching question library

## Versioning and release process

Each plugin versions and ships independently using a plugin-specific tag prefix. The repo uses semver in each plugin's `plugin.json`.

| Plugin | Tag pattern | Workflow |
|---|---|---|
| `product-in-acquisitions-os` | `pia-v<version>` | `.github/workflows/release-pia.yml` |
| `job-interview-meeting-preparation` | `interview-v<version>` | `.github/workflows/release-interview.yml` |

Cut a release by tagging with the right prefix and pushing the tag:

```bash
# Product in Acquisitions OS
git tag pia-v0.1.1
git push origin pia-v0.1.1

# Job Interview Meeting Preparation
git tag interview-v0.1.0
git push origin interview-v0.1.0
```

Each workflow triggers only on its prefix, packages just its own plugin into a `.plugin` file (which is a zip with a custom extension), and attaches it to a plugin-specific GitHub release. Subscribers download the latest from the stable Releases URL.

When you bump the version in a plugin's `plugin.json`, make the same bump in that plugin's git tag.

When adding another plugin in the future, follow the same pattern: pick a short tag prefix (e.g. `<short-name>-v*`), add a dedicated `release-<short-name>.yml` workflow, and the existing workflows are unaffected.

## Marketplace install

The repo root contains `.claude-plugin/marketplace.json` which lists this plugin. Users install with:

```bash
claude plugin install enalbenerraw/blanewarrene
```

If you add more plugins to the repo over time, add them as additional entries in `marketplace.json`.

## What Claude Code should do next

The plugin is complete and tested. The handoff tasks remaining are:

1. **Copy the staged files into the repo.** The `init_repo.sh` script in this handoff bundle does this; review it before running.
2. **Run validation locally.** Confirm `plugin.json` is valid JSON, all four skills have valid frontmatter, and the directory structure matches the layout above.
3. **Commit with a descriptive message.** Suggested first commit: `Add product-in-acquisitions-os plugin (v0.1.0)`.
4. **Push to main, then tag and push the tag** to trigger the release workflow.
5. **Update the repo README** at the root with a "Plugins" section pointing to `plugins/product-in-acquisitions-os/README.md`.

## What NOT to do

- Do not modify the SKILL.md files unless I explicitly ask. They have been hand-tuned for tone and trigger phrasing.
- Do not add em dashes anywhere. Run a `grep -r "—" plugins/product-in-acquisitions-os/` check before committing.
- Do not regenerate template content. The 25 reference templates under `skills/*/references/` are the source of truth.
- Do not change the attribution footer format.

## Related external assets

- Framework PDF: `The-90-Day-Product-Integration-Framework (1).pdf` (in author's local Cowork folder, not in repo)
- Substack: blanewarrene.substack.com (premium tier distributes the plugin)
- Eventual Teachable course: outline staged in author's Cowork folder, not yet in repo

## Contact

Blane Warrene · enerrawenalb@gmail.com · 919-208-3899
