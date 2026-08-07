# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2026-08-07

Found by running `tech-stack-inventory` against a 62-person third-party
logistics company on the first real pass.

### Fixed

- **The `Cost basis` enum was too narrow.** It allowed published list, reported
  by you, or estimated. At 25 to 150 people the tools that matter most are
  usually the ones with no public pricing at all: the TMS, the ERP, the payroll
  system. A homegrown internal tool has no cost basis either. Added
  `quote-based` and `none`, with guidance that quote-based is a real answer
  rather than a gap to fill in later.
- Added explicit guidance to prefer `unknown` over a guess in the AI column.
  Which AI tier a plan includes varies by contract, and asserting the wrong one
  in a document someone reads to a board is worse than admitting it was not
  checked.

## [0.1.0] - 2026-08-07

Initial release. Converts the AI SMB Toolkit from four blank Word templates
into four skills that interview the operator and produce completed documents.

### Added

- `tech-stack-inventory`. Interviews the operator, then produces a populated
  inventory of what the company runs, what each tool costs, who owns it, and
  where AI fits or is already redundant.
- `ai-readiness-survey`. Generates an employee survey tuned to org size and
  vertical, designed to surface the AI use already happening informally, plus
  distribution guidance and a rubric for reading the results.
- `prompt-cookbook`. Builds prompt workflows for the company's actual vertical
  and roles rather than generic examples, each with the job it does and how to
  tell whether it worked.
- `enablement-course`. Assembles an internal AI enablement course from the
  outputs of the other three, sized to the company's real starting point.

### Notes

- The four Word documents in `prompts/ai-smb-toolkit/` remain available and are
  marked portable. They serve the download audience that will never open a
  Claude surface. Both are maintained.
- Skills run standalone. Each closes by naming the natural next one; nothing
  chains automatically.
