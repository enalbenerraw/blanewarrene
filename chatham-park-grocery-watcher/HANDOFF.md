# Handoff: move to its own private repo and go live

Paste the prompt below into Claude Code in a terminal, in an empty folder where you keep projects. It assumes the GitHub CLI (`gh`) is installed and signed in (`gh auth status`). If it is not, run `gh auth login` first.

---

```text
Set up my Chatham Park Grocery Watcher as its own private GitHub repo and take it live.

The finished code is in the folder chatham-park-grocery-watcher/ on branch
claude/stoic-wozniak-8uvukj of enalbenerraw/blanewarrene. That folder is already laid
out as a standalone repo (files at its root, its own .github/workflows/watch.yml).

1. Extract it into a new local folder and make it a repo:
     git clone --depth 1 --branch claude/stoic-wozniak-8uvukj https://github.com/enalbenerraw/blanewarrene.git /tmp/bw-handoff
     cp -R /tmp/bw-handoff/chatham-park-grocery-watcher ./chatham-park-grocery-watcher
     rm -rf /tmp/bw-handoff
     cd chatham-park-grocery-watcher && rm HANDOFF.md
     git init -b main && git add -A && git commit -m "Add Chatham Park grocery watcher"
   Confirm .github/workflows/watch.yml made it across (dotfolders are easy to drop).
2. Read CLAUDE.md, then run the offline tests: python3 -m pip install -r requirements.txt
   and python3 -m unittest test_watcher -v. Stop and tell me if anything fails.
3. Run python3 watcher.py --check-sources locally. Fix any FAIL line by finding the
   correct URL or parsing (local news feed URLs and the Pittsboro CivicPlus Agenda
   Center are unverified). Then run python3 watcher.py --dry-run and show me the digest.
   Commit any fixes, with the tests still passing.
4. Create the private repo and push:
     gh repo create chatham-park-grocery-watcher --private --source . --push
5. Set workflow permissions to read and write so the job can save seen.json:
     gh api -X PUT repos/{owner}/chatham-park-grocery-watcher/actions/permissions/workflow \
       -f default_workflow_permissions=write
6. Secrets. Ask me for my Gmail address and remind me to create an app password at
   https://myaccount.google.com/apppasswords (2-Step Verification must be on). Have ME
   enter the values with `gh secret set SMTP_USER`, `gh secret set SMTP_PASSWORD`, and
   `gh secret set EMAIL_TO`, which prompt for the value, so the password never passes
   through this chat. Do not echo or log any secret.
7. Trigger the workflow in this order, waiting for each to finish (gh run watch) and
   reading its log: mode=check-sources, mode=test-email, mode=normal, then mode=normal
   again.
     gh workflow run watch.yml -f mode=check-sources
   Done when the first normal run emails me a digest of real recent Chatham Park items
   and the second normal run sends nothing. Confirm seen.json was committed by the bot.
8. Tell me when it is live, then I will close the old draft PR in enalbenerraw/blanewarrene
   (pull request 9). Do not merge that PR.

Rules: no em dashes in anything you write; keyword and source changes go in config.yaml,
not code; keep the README readable by a non-developer.
```

---

## What you will need on hand

- About 15 minutes.
- Your phone, for Google 2-Step Verification if it is not already on.
- The Gmail address the alerts should come from, and where they should go.
