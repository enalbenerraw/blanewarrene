# Changelog

All notable changes to this skill are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
