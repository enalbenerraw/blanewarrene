# Changelog

All notable changes to this skill are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.2] - 2026-08-07

### Fixed

- **Artifact emission named a tool that does not exist in Cowork.** The skills
  instructed a call to `Artifact`. Cowork exposes `mcp__cowork__create_artifact`,
  which takes a self-contained HTML page, plus `mcp__visualize__show_widget` for
  inline rendering. Nothing named `Artifact` is there, so the instruction was
  unactionable and the artifact was silently skipped.
- Delivery now names the tool per surface: `mcp__cowork__create_artifact` in
  Cowork, `Artifact` in Claude Code and claude.ai, with the title required
  either way. Markdown-producing skills wrap their document in minimal
  self-contained HTML for Cowork; skills that already emit HTML pass it through.
- **The artifact was also worded as an option rather than a requirement.**
  Delivery led with a satisfiable imperative and then listed surfaces as
  bullets, so once the file was written the artifact read as one choice among
  several. One skill attempted the call, another skipped it, on near-identical
  wording.

## [0.5.1] - 2026-08-07

Found by running the plugin in Cowork, which is the first time these skills
executed outside Claude Code.

### Fixed

- **`signal-watch` referenced the Artifact tool without granting it.** Its body
  said "emit as a markdown artifact" while `allowed-tools` omitted `Artifact`.
- **No skill documented that the artifact call requires a title.** Cowork
  rejects the call without one, which surfaced as a non-blocking widget error
  on the first real Cowork run. All five skills now state the requirement and
  give the title to use.
- **`strategic-gtm-intel` and `pre-call-briefing` had no artifact path at all.**
  Both produce markdown documents, so in Cowork they wrote to disk and rendered
  nothing. Both now grant `Artifact` and carry the same delivery block as their
  siblings.

### Notes

- Confirmed by that run: plugins install in Cowork through Customize, and
  `when_to_use` survives the plugin path. The six-field Agent Skills frontmatter
  limit applies to claude.ai skill uploads, not to plugin skills, so these
  skills work in Cowork unchanged.
- `claude plugin validate --strict` passed on every version that shipped these
  defects. Manifest validation does not check whether a skill body references a
  tool the frontmatter withholds.

## [0.5.0] - 2026-08-07

The plugin becomes a market-intelligence suite. Four new skills join the
original, all sharing the hardened `entity-researcher` subagent.

### Added

- **`signal-watch`**. Executive briefing on one company: fundamentals, an
  executive leadership map, public messaging analysis over a chosen window,
  and a selling-versus-signaling synthesis. Unconfirmed leadership roles are
  written as unconfirmed rather than guessed, because an executive who
  name-drops a CRO who left eight months ago pays for that in the room.
- **`competitive-brief-generator`**. One focal company against six to eight
  researched rivals, rendered as a three-page styled HTML brief plus PDF where
  a code environment is available: competitive landscape, product catalog by
  buyer center, and a win/qualify/route-around battle card. The house-style
  stylesheet ships in `references/` and is used verbatim so every brief looks
  like it came from the same shop.
- **`strategic-gtm-intel`**. Two-sided competitive wedge analysis: your company
  against one named competitor. Audits paid and organic messaging, identifies
  messaging drift and persona pivots, drafts trap-setting questions for sales,
  and closes with a four-bullet board summary naming the aggressor claim, the
  alignment opportunity, the pipeline segment at risk, and one GTM adjustment
  for next week.
- **`pre-call-briefing`**. Executive-grade briefing for a commercial call
  already on the calendar. Runs a clarifying interview first, then a
  seven-source research protocol, and closes with a call playbook and a single
  provocation rather than a summary.

### Changed

- **displayName is now "Market Intelligence".** The plugin `name`, the
  `source` path, the `clb-v*` tag prefix, `release-clb.yml`, and the stable
  Releases URL are all unchanged, so existing installs, tags, and download
  links keep working. Only the human-readable name moved.
- **Every skill's `when_to_use` now names its routing discriminator and points
  at the others.** Five skills that all research a company is a real routing
  risk, so the discriminators are explicit: entity count, whether your own
  company is one of the two sides, whether a call is on the calendar, and
  output shape. The original skill was edited too, since a discriminator
  stated on one side only does not disambiguate.
- All four new skills reuse `entity-researcher` rather than duplicating
  research logic, which keeps the third-party verification pass and the
  prompt-injection defense in exactly one place. `strategic-gtm-intel` is the
  clearest case: it is two-sided, so it sends posture `standalone` with the
  peer named. Before 0.4.1 parameterized that subagent, it forbade comparison
  outright and this skill could not have been built on it.

### Notes

- The source prompts remain in the repo and are marked portable. They run in
  any capable AI tool; the skills add a verified research subagent and file
  output. Both are maintained.

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
