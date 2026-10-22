# Project: Chatham Park Grocery Watcher

A small monitor that runs daily on GitHub Actions and emails a digest when there is news about which grocery chain will anchor the new mixed-use center near the Chatham Park YMCA in Pittsboro, NC. In September 2026, Chatham Park said that center would be anchored by "Chatham Park's next grocery store", without naming the chain. A Lowes Foods already opened at Northwood Landing in 2023; that is old news and must not trigger an alert on its own.

## Layout

| File | Purpose |
|---|---|
| `watcher.py` | The whole program. Fetches sources, matches, dedupes, emails, saves state. |
| `config.yaml` | Every keyword, source URL, and email setting. The owner edits this by hand on GitHub. |
| `seen.json` | Memory of what was already sent. Created on the first real run and committed back by the workflow. Do not edit by hand. |
| `.github/workflows/watch.yml` | Daily schedule (11:00 UTC), manual run with modes: normal, dry-run, check-sources, test-email. |
| `test_watcher.py` | Offline tests with canned responses. No network needed. |
| `README.md` | Setup guide written for a non-developer. Keep it that way. |

## How it works

1. **Sources.** Google News RSS searches (configured queries plus one `"Chatham Park" <chain>` per chain). Local news feeds (Chatham News + Record, Chapelboro, Chatham Journal), each with fallback URLs tried in order. Town of Pittsboro CivicPlus Agenda Center (`/RSSFeed.aspx?ModID=65&CID=All-0`, `/AgendaCenter`, `/AgendaCenter/Search/`), filtered to Board of Commissioners and Planning Board, downloading `?packet=true` PDFs and extracting text with pypdf.
2. **Matching.** Flag only if the text has a location term AND a grocery term (generic word or chain). Case-insensitive, tolerant of apostrophes, hyphens, and plurals.
3. **Low priority.** If an item mentions a `low_priority_terms` entry (Lowes Foods, Northwood Landing), names no other chain, and has no `new_store_phrases` match, it is held in `state["pending_low"]` and never emails alone. It rides along with the next real digest or weekly heartbeat.
4. **Dedupe.** News is keyed by normalized URL, title hash, and title+link hash. Agenda packets are keyed by document ID plus the set of grocery terms found, so an amended packet naming a new chain alerts again. Upcoming meetings are re-scanned each run; past meetings are scanned once.
5. **Email.** One digest per run via Gmail SMTP (app password) or Resend. Nothing new means no email, except an optional weekly heartbeat. State is saved only after a send succeeds, so a failed send retries next run.
6. **Resilience.** Each source is wrapped. A failed source is logged, listed in the email footer, and raises a workflow warning. The run fails only if every source fails.

## Secrets (GitHub Actions)

`SMTP_USER`, `SMTP_PASSWORD` (Gmail app password), `EMAIL_TO` (optional, comma-separated), `EMAIL_FROM` (optional), `RESEND_API_KEY` (only if `provider: resend`). Never put credentials in code or config.

## Verification status

- Offline tests pass: `python -m unittest test_watcher -v`.
- **Never run against the live web.** It was built in a sandbox that blocked news.google.com, pittsboronc.gov, and the local news sites. Unconfirmed assumptions:
  - The local news feed URLs in `config.yaml` (standard WordPress `/feed/` paths). Chatham Journal's domain was not confirmed to exist.
  - The CivicPlus Agenda Center HTML structure (board name taken from the nearest preceding `h2`/`h3`) and the `ModID=65` RSS feed.
  - Google News RSS titles end in ` - <Source>`, which the code strips.
- The first `check-sources` run on Actions is the real test. Fix any `FAIL` lines by correcting URLs in `config.yaml` or parsing in `watcher.py`.

## Done when

1. A manual `normal` run finds real recent articles about Chatham Park retail and emails a digest.
2. A second `normal` run right after sends nothing.

## Conventions

- No em dashes anywhere, including the README and emails. Use commas, parentheses, or separate sentences.
- Keep it simple: one script plus one config file. Do not add a framework or database.
- Keyword and source changes belong in `config.yaml`, not in code.
- The README audience is a non-developer. Write steps as clicks, not commands, where possible.
- Run `python -m unittest test_watcher -v` before every commit.
