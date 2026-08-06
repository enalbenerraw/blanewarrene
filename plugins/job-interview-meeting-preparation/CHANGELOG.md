# Changelog

All notable changes to this skill are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2026-08-06

### Security

- Both research subagents now refuse instructions embedded in fetched pages.
  `company-researcher` and `stakeholder-researcher` hold `WebSearch` and
  `WebFetch` but carried no prompt-injection defense, while the sibling
  `entity-researcher` in `comparative-landscape-brief` already had one.
  A `Flagged content` section reports any attempt.

### Added

- Verification pass on `company-researcher`. Quantitative self-claims
  (revenue, growth, customer count, headcount, funding, valuation) must be
  corroborated by a filed or audited source, or by a credible third party,
  before they are stated as fact. Everything else is labeled
  company-reported.
- Verification pass on `stakeholder-researcher`. Titles, tenure, team size,
  and credited outcomes usually originate with the person, so claims found
  only in self-authored material are labeled self-reported.
- `Data caveat` section on both subagents' output, naming which figures are
  unverified.
- Step 3 of the skill now has explicit handling for `Data caveat` and
  `Flagged content`, so neither can be silently dropped by the orchestrating
  conversation. Caveats must survive into the one-pager, which is the
  artifact read under pressure.
- Two edge cases covering flagged content and unverifiable stakeholder
  claims.

## [0.3.0] - 2026-07-24

### Added

- `agents/company-researcher.md` subagent that researches one company at a
  full or abbreviated depth level and returns a structured dossier.
- `agents/stakeholder-researcher.md` subagent that gathers raw public-record
  findings on one stakeholder when no LinkedIn PDF is supplied.
- `allowed-tools` scoping on the skill.
- `displayName` on the plugin manifest and marketplace entry.

### Changed

- Primary company, secondary company, and stakeholder research now run in
  parallel as subagents instead of sequentially in the orchestrating
  conversation.
- Stakeholder synthesis stays in the orchestrating conversation. The
  subagent returns raw findings only, because the interpretive read needs
  the company dossier alongside them.
- Skill frontmatter split into separate `description` and `when_to_use`
  fields.

## [0.2.0] - 2026-06-03

### Added

- Surface-aware delivery for the one-pager: HTML artifact on claude.ai web,
  `present_files` on a Cowork hosted session, and `~/Documents` with
  reported paths on local Claude Code.
- README note documenting the local Playwright dependency for rendering the
  one-pager PDF.

### Changed

- The one-pager is never left inline-only. The PDF leads on every surface.

## [0.1.0] - 2026-05-07

### Added

- Initial public release.
- `SKILL.md` with the seven-step methodology covering input capture, plan
  announcement, primary company research, secondary company research,
  stakeholder analysis (LinkedIn PDF or web), conversation architecture, and
  dual-deliverable output.
- `references/one-pager-template.html` editorial-style one-pager template.
- Coverage for four meeting types: interview (default), advisory or
  consulting, partnership or BD, and sales discovery.
- Sanitized worked example in `examples/`.
