# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-11-22

### Added

- Four subagents with hard role boundaries: `explorer` (Haiku, low effort,
  read-only discovery), `implementer` (Sonnet, medium effort, scoped changes,
  never commits or deploys on its own), `reviewer` (Opus, high effort, plan
  and diff review), and `researcher` (Sonnet, medium effort, sourced web
  research and read-only Notion lookups).
- Length caps on every agent's report (150 to 300 words, or at most 7 ranked
  findings for the reviewer), so the main session does not pay its own model's
  input rate to re-read long answers.
- `fleet-routing` skill: when to delegate, the standard explore, plan, build,
  review sequence, and what stays with the main agent.
