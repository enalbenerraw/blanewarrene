# GTM Intel CLI

A messaging analysis tool for product managers. Analyze competitor, strategic partner, and your own public messaging using Gemini with Google Search grounding, and log results to Google Sheets.

## What It Does

GTM Intel runs three types of analysis on paid and organic content from the past 7 days:

- **Competitive Analysis** — Extracts core themes, claims, and target personas from competitor messaging across social media and their website.
- **Strategic Partner Analysis** — Same analysis for partners, plus identifies specific opportunities for your company to interact with or amplify their content via your own GTM activity.
- **Self-Inspect** — Audits your own messaging for themes, consistency, and gaps.

Each mode can be run individually or batched together. Results are logged to a Google Sheet with one tab per mode for easy week-over-week tracking.

## Prerequisites

- Python 3.11+
- A [Gemini API key](https://aistudio.google.com/apikey)
- A Google Cloud service account with the Sheets API enabled
- A Google Sheet shared with the service account email

## Setup

1. **Clone and install:**

   ```bash
   cd blanewarrene
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e .
   ```

2. **Configure environment variables:**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and fill in:

   | Variable | Description |
   |----------|-------------|
   | `GEMINI_API_KEY` | Your Gemini API key |
   | `GOOGLE_SHEETS_ID` | The ID from your Google Sheet URL (the long string between `/d/` and `/edit`) |
   | `GOOGLE_SERVICE_ACCOUNT_FILE` | Path to your service account JSON (default: `credentials/service-account.json`) |

3. **Set up Google Sheets access:**

   - Create a project in [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the Google Sheets API
   - Create a service account and download the JSON key file
   - Place the JSON file in `credentials/service-account.json`
   - Open your target Google Sheet and share it (Editor access) with the `client_email` from the JSON file

## Usage

```bash
source .venv/bin/activate
gtm-intel
```

The tool will walk you through:

1. Enter your company name and URL
2. Add one or more competitors (name + URL each)
3. Optionally add strategic partners
4. Select analysis mode: Competitive, Partners, Self-Inspect, or Run All
5. Confirm and run

Results are displayed in the terminal and logged to your Google Sheet.

## Google Sheets Output

The tool creates three tabs in your spreadsheet:

| Tab | Columns |
|-----|---------|
| `competitive` | Run Date, Company Name, URL, Core Themes, Context Summary, Key Claims, Target Personas, Raw Analysis |
| `partners` | Run Date, Company Name, URL, Core Themes, Context Summary, Key Claims, GTM Opportunities, Raw Analysis |
| `self_inspect` | Run Date, Company Name, URL, Core Themes, Context Summary, Key Claims, Messaging Gaps, Raw Analysis |

Tabs and headers are created automatically on first run.

## Project Structure

```
src/gtm_intel/
├── cli.py          # Interactive prompts and orchestration
├── config.py       # Environment variable loading and validation
├── models.py       # Company and AnalysisResult data models
├── prompts.py      # Prompt templates for each analysis mode
├── analyzer.py     # Gemini API calls with Google Search grounding
├── sheets.py       # Google Sheets logging
└── auth.py         # API authentication and validation
```
