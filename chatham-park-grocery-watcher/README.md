# Chatham Park Grocery Watcher

A small robot that checks the web every morning and emails you when there is news about which grocery chain is coming to the new mixed-use center near the Chatham Park YMCA in Pittsboro, NC. It runs free on GitHub Actions, so no computer needs to stay on.

## What it checks

| Source | How |
|---|---|
| Google News | About 20 searches, such as `"Chatham Park" grocery`, `Pittsboro grocery store`, and one per chain (`"Chatham Park" Publix`, `"Chatham Park" Harris Teeter`, and so on) |
| Local news | Chatham News + Record, Chapelboro, and Chatham Journal feeds, plus Google News searches limited to each of those sites (a backup if a site's own feed breaks) |
| Town of Pittsboro agendas | The town's CivicPlus Agenda Center (pittsboronc.gov/AgendaCenter). It finds Board of Commissioners and Planning Board meetings, downloads the full agenda packet PDF, and searches the text. Site plans often name a tenant before any press release. |

An item is flagged only if it mentions a **place** (Chatham Park, Pittsboro, Mosaic, YMCA, South Village, North Village) **and** a **grocery term** (grocery, supermarket, anchor tenant, or a chain name).

Stories that are only about the existing Lowes Foods at Northwood Landing are marked **lower priority**. They never trigger an email by themselves. They ride along at the bottom of the next real alert or weekly heartbeat.

## What the email looks like

Subject: **Chatham Park grocery watch: 3 new mentions**

Each mention shows the headline (linked), source, date, which keywords matched, and the matching passage with keywords highlighted. At the bottom, a one-line health check says how many sources worked, and names any that failed.

If nothing new turned up, no email is sent. Once a week (Monday by default) you get a short "no new mentions this week" email so you know it is still running. You can turn that off.

---

## Setup (about 15 minutes, no coding)

The watcher lives in the `chatham-park-grocery-watcher` folder of this repository, and its schedule lives in `.github/workflows/chatham-grocery-watch.yml`. GitHub only runs scheduled jobs from the repository's main branch, so this must be merged into `main` before the daily run starts.

> **Want it in its own repository instead?** Create a new private repo on GitHub, then upload the `chatham-park-grocery-watcher` folder and the `.github/workflows/chatham-grocery-watch.yml` file into it, keeping the same folder layout. Everything below works the same way.

### Step 1. Get a Gmail app password

Gmail will not let a program use your normal password. You create a separate 16-character "app password" for this one purpose.

1. Go to [myaccount.google.com/security](https://myaccount.google.com/security).
2. Under "How you sign in to Google", turn on **2-Step Verification** if it is not already on. App passwords require it.
3. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
4. Type a name such as `Grocery watcher` and click **Create**.
5. Copy the 16-letter password Google shows you. You will paste it in Step 2. (Spaces in it are fine.)

You can revoke it from the same page at any time without affecting your normal Gmail password.

### Step 2. Add your secrets to GitHub

Secrets are stored encrypted by GitHub. They never appear in the code or the logs.

1. On GitHub, open this repository and click **Settings** (top right of the repo page).
2. In the left menu, click **Secrets and variables**, then **Actions**.
3. Click **New repository secret** and add each of these:

| Name | Value |
|---|---|
| `SMTP_USER` | Your Gmail address, for example `you@gmail.com` |
| `SMTP_PASSWORD` | The app password from Step 1 |
| `EMAIL_TO` | Where alerts go. Can be the same address. For several people, separate with commas. Optional: defaults to `SMTP_USER`. |

### Step 3. Allow the robot to save its memory

The watcher remembers what it already sent by saving a small file (`seen.json`) back into the repository after each run.

1. **Settings**, then **Actions**, then **General**.
2. Scroll to **Workflow permissions**, choose **Read and write permissions**, and click **Save**.

### Step 4. Test it

Go to the **Actions** tab, click **Chatham Park grocery watch** in the left list, then **Run workflow**. A menu lets you pick a mode. Run them in this order:

1. **check-sources**. Confirms each source can be reached. Open the run, click the `watch` job, and read the `Run watcher` step. Every line starts with `OK` or `FAIL`.
2. **test-email**. Sends you a one-line test email. If this fails, recheck the secrets in Step 2.
3. **dry-run**. Finds matches and prints the digest in the log, but sends nothing and remembers nothing. Use this any time you change keywords.
4. **normal**. The real thing. You should receive a digest of recent mentions.
5. **normal** again, right away. You should receive nothing, because those items were already sent.

After that, it runs by itself every morning.

---

## Changing the schedule

Open `.github/workflows/chatham-grocery-watch.yml` on GitHub and click the pencil icon. Find this line:

```yaml
    - cron: "0 11 * * *"
```

The time is in UTC. `11` means 7am Eastern in summer and 6am in winter.

| You want | Change the line to |
|---|---|
| Daily, about 7am Eastern | `- cron: "0 11 * * *"` (the default) |
| Weekly, Monday morning | `- cron: "0 11 * * 1"` |
| Twice a week, Monday and Thursday | `- cron: "0 11 * * 1,4"` |
| Daily, about 9pm Eastern | `- cron: "0 1 * * *"` |

Click **Commit changes**. GitHub sometimes starts scheduled runs a few minutes late; that is normal.

To turn the weekly "nothing new" email off, or move it to a different day, edit `weekly_heartbeat` and `heartbeat_day` at the bottom of `config.yaml`.

## Editing keywords and sources

Everything the watcher looks for is in `chatham-park-grocery-watcher/config.yaml`. Open it on GitHub, click the pencil icon, edit, and commit. Each section has a short note explaining it. Common edits:

- **Add a chain:** add a line under `grocery_chains`, for example `  - Costco`. Keep the two spaces and the dash. A Google News search for `"Chatham Park" Costco` is added automatically.
- **Add a place:** add a line under `location_terms`.
- **Add a search:** add a line under `google_news: queries:`. Wrap exact phrases in single quotes on the outside and double quotes inside, like `'"Chatham Park" retail'`.
- **Look further back:** raise `max_age_days`.
- **Scan more town boards:** add a word from the board's name under `town_agendas: boards:`, or empty the list to scan every board.

After editing, run the workflow in **dry-run** mode to check the result before the next real run.

Matching ignores capitals and small spelling differences: `Lowe's Foods` matches `Lowes Foods`, `Trader Joes` matches `Trader Joe's`, and plurals match.

## Using Resend instead of Gmail (optional)

1. Create a free account at [resend.com](https://resend.com) and create an API key.
2. Add the secret `RESEND_API_KEY`, and `EMAIL_TO`.
3. In `config.yaml`, change `provider: gmail` to `provider: resend`.

Without a verified domain, Resend only delivers to the email address on your Resend account. To send from your own domain, verify it in Resend and add an `EMAIL_FROM` secret such as `Grocery Watch <alerts@yourdomain.com>`.

## Troubleshooting

| Symptom | Likely cause and fix |
|---|---|
| Run shows a red X with "Missing secret" | A secret name is misspelled or missing. Names must match Step 2 exactly. |
| `Username and Password not accepted` | Use the app password, not your Gmail password, and confirm 2-Step Verification is on. |
| Run is green but has a yellow warning | One or more sources failed and the rest ran normally. The email footer and the log name the failed source. A site being down for a day is normal. If one fails every day, its address probably changed: update its URL in `config.yaml`. |
| "Save memory" step fails with `permission denied` | Step 3 was skipped. |
| Same item emailed twice | Usually the same story under two different headlines and links. Rare, and harmless. |
| Daily runs stopped | GitHub pauses schedules on public repositories after 60 days without activity. Open the Actions tab and click **Enable workflow**. |

## Running it on your own computer (optional)

```bash
cd chatham-park-grocery-watcher
pip install -r requirements.txt
python watcher.py --check-sources
python watcher.py --dry-run
python -m unittest test_watcher -v   # offline tests, no network needed
```

To send real email locally, set `SMTP_USER`, `SMTP_PASSWORD`, and `EMAIL_TO` as environment variables first.

## Known limits

- Google News gives only a headline and a one-line summary, so a story that names the chain deep in the article and not in the headline or summary can be missed. The chain-specific searches reduce this risk.
- Agenda packets that are scanned images (no selectable text) cannot be searched. Most Pittsboro packets are text PDFs.
- Packets over 60 MB are skipped so a single giant file cannot stall a run. Change `max_file_mb` in `config.yaml` to raise the limit.
