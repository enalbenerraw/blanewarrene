# Changelog

All notable changes to this skill are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.3] - 2026-08-07

### Fixed

- Install instructions. `claude plugin install` takes a plugin name, not a
  repo, so the published command failed with "not found in any configured
  marketplace". Corrected to `claude plugin marketplace add` followed by
  `claude plugin install <name>@blanewarrene-marketplace`, and notes that
  `/reload-plugins` applies the change to a running session.

## [0.4.2] - 2026-08-07

### Changed

- Attribution footer on generated deliverables is now `Created by Blane
  Warrene, blanewarrene.com`. blanewarrene.com is the canonical home;
  Substack syndicates and is linked from the repo README rather than from
  deliverables. One string across every plugin, so the per-plugin variants
  that had drifted cannot recur.

## [0.4.1] - 2026-08-07

### Added

- `LICENSE`. The manifest has declared MIT since this plugin shipped, but no
  license text was present, so the grant was asserted and never made. The
  `clb-v0.4.0` release does not contain it; this one does.

### Changed

- `homepage` now points to blanewarrene.com, the canonical owner of this
  content, rather than to the Substack that distributes it.

## [0.4.0] - 2026-08-06

### Changed

- `entity-researcher` is no longer hardwired to comparative work. It takes a
  research posture, either `one of a parallel set` or `standalone`, which
  decides one thing: whether comparison is the subagent's job. This skill
  always sends `one of a parallel set`, matching its previous behavior, since
  sibling instances cannot see each other's findings and the comparing
  happens in Step 4. The prior text asserted the parallel-set situation as a
  fact rather than a parameter, so the subagent could not be reused by any
  skill that researches one entity at a time.
- The messaging-themes heading now carries the time window it was given.
  Previously the output template hardcoded `### 90-day messaging themes`
  while Step 2 already accepted the window as a parameter, so any window
  other than 90 days produced findings filed under a heading that
  contradicted them. `brief-structure.md` and the Step 5 per-entity template
  were carrying the same hardcoded heading and now defer to what the dossier
  returns.
- The subagent description and output-format preamble describe the work
  rather than naming this one calling skill.

### Notes

- No behavior change for this skill's own users. Default window is still
  90 days and the parallel-set posture is what it always did implicitly.

## [0.3.0] - 2026-07-24

### Added

- `agents/entity-researcher.md` subagent that researches and verifies one
  named entity and returns a structured dossier covering messaging themes,
  inferred strategic priorities, a leverageable tailwind, verification
  status, and sources.
- `allowed-tools` scoping on the skill.
- `displayName` on the plugin manifest and marketplace entry.

### Changed

- Entity research now fans out in parallel, one subagent per entity, instead
  of researching the set sequentially. Cross-entity synthesis stays in the
  orchestrating conversation; each subagent sees only its own entity.
- Subagents fall back to reasonable defaults (3 to 5 lens dimensions, a
  90-day window) rather than asking questions the spawning conversation
  cannot answer.
- Skill frontmatter split into separate `description` and `when_to_use`
  fields.

## [0.2.0] - 2026-06-03

### Changed

- Step 7 output is surface-aware: a markdown artifact on claude.ai web,
  `present_files` on a Cowork hosted session, and the Step 1 path (default
  `~/Documents/<slug>-brief.md`) on local Claude Code. The brief is never
  left inline-only.
- Step 1 output destination now scopes its default to local-disk delivery
  and points at Step 7 for surface handling.

## [0.1.0] - 2026-05-13

### Added

- Initial public release.
- `SKILL.md` with the seven-step methodology covering input capture, per
  entity research, 90-day messaging analysis, third-party verification of
  quantitative claims, cross-cutting synthesis, and a single markdown brief.
- Coverage for 3 to 8 entities across organizations, products, and
  initiatives.
- Audience framing for investors, board, exec team, M&A committee, partners,
  and advisory or customer advisory boards.
