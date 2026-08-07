# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
