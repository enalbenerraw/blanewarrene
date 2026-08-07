# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.1] - 2026-08-07

### Changed

- Attribution footer on generated deliverables is now `Created by Blane
  Warrene, blanewarrene.com`. blanewarrene.com is the canonical home;
  Substack syndicates and is linked from the repo README rather than from
  deliverables. One string across every plugin, so the per-plugin variants
  that had drifted cannot recur.

## [0.5.0] - 2026-08-07

### Changed

- **Relicensed from `LicenseRef-Proprietary` to MIT.** Every plugin in this
  marketplace is now MIT, which removes the inconsistency where two were
  permissive and one was not. This grant is irrevocable for this version and
  any later one carrying it: MIT permits redistribution, modification, and
  commercial resale.
- `homepage` now points to blanewarrene.com, the canonical owner of this
  content, rather than to the Substack that distributes it.

### Added

- `LICENSE`. The manifest previously declared a license with no license text
  present, so the terms were asserted and never stated.

## [0.4.0] - 2026-07-28

### Added

- `allowed-tools` scoping on all four skills.
- `AskUserQuestion` in the allowed tools, so the calibration questions run as
  a structured prompt rather than free text.
- `displayName` on the plugin manifest and marketplace entry.

### Changed

- Skill frontmatter split into separate `description` and `when_to_use`
  fields across all four skills.
- Wording tightened in `references/calibration.md`.

## [0.3.0] - 2026-06-03

### Added

- `references/durable-output.md` describing surface-aware delivery.

### Changed

- All four skills deliver their produced markdown durably rather than
  inline: an artifact on claude.ai web, `present_files` on a Cowork hosted
  session, and `~/Documents` on local Claude Code.

## [0.2.0] - 2026-05-27

### Added

- `references/calibration.md` with scope calibration for acquirers up to $5B
  enterprise value, covering the well-funded early stage (sub-$100M ARR) and
  mature growth stage ($100M to $500M ARR) shapes.
- Three calibration questions at the open of each skill covering company
  stage, acquisition shape, and prior integration experience. They tune the
  depth, stakeholder breadth, and pacing of every downstream deliverable.
- README section documenting where the framework fits and where it does not.

## [0.1.0] - 2026-05-05

### Added

- Initial release of the 90-Day Product Integration Framework as a plugin.
- `week-0-readiness` skill: integration lead charter, decision rights
  one-pager, combined product narrative, customer commitment inventory, and
  the five-question Day 1 readiness check.
- `roadmap-convergence` skill: roadmap map, conflict log, three session
  facilitation guides, merged 90-day plus 12-month roadmap, and the 30/60/90
  execution plan.
- `positioning-stability` skill: positioning statement, sales FAQ, talk
  track, competitive response scripts, top-20 outreach plan, and advisory
  council charter.
- `people-integration` skill: decision map session template, mentor pairing
  matrix, 30/60/90 ownership plan, retention risk review, and the 1:1
  coaching question library.
- Reference templates under `skills/*/references/` as the source of truth for
  every deliverable.
