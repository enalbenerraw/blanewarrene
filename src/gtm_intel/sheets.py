"""Google Sheets integration for logging analysis results."""

import gspread

from gtm_intel.models import AnalysisResult

TAB_HEADERS = {
    "competitive": [
        "Run Date", "Company Name", "URL", "Core Themes",
        "Context Summary", "Key Claims", "Target Personas", "Raw Analysis",
    ],
    "partners": [
        "Run Date", "Company Name", "URL", "Core Themes",
        "Context Summary", "Key Claims", "GTM Opportunities", "Raw Analysis",
    ],
    "self_inspect": [
        "Run Date", "Company Name", "URL", "Core Themes",
        "Context Summary", "Key Claims", "Messaging Gaps", "Raw Analysis",
    ],
}

MAX_CELL_LENGTH = 49000  # Google Sheets cell limit is 50k chars


def ensure_tabs(client: gspread.Client, sheet_id: str) -> None:
    """Create worksheet tabs if they don't exist and add headers."""
    spreadsheet = client.open_by_key(sheet_id)
    existing = [ws.title for ws in spreadsheet.worksheets()]

    for tab_name, headers in TAB_HEADERS.items():
        if tab_name not in existing:
            worksheet = spreadsheet.add_worksheet(tab_name, rows=1, cols=len(headers))
            worksheet.append_row(headers)
        else:
            worksheet = spreadsheet.worksheet(tab_name)
            first_row = worksheet.row_values(1)
            if not first_row:
                worksheet.append_row(headers)


def log_result(client: gspread.Client, sheet_id: str, result: AnalysisResult) -> None:
    """Append a single analysis result as a row in the appropriate tab."""
    spreadsheet = client.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet(result.mode)

    raw = result.raw_response[:MAX_CELL_LENGTH] if result.raw_response else ""

    row = [
        result.run_date,
        result.company.name,
        result.company.url,
        ", ".join(result.core_themes),
        result.context_summary,
        result.key_claims,
        result.mode_specific,
        raw,
    ]
    worksheet.append_row(row, value_input_option="RAW")


def log_results(
    client: gspread.Client, sheet_id: str, results: list[AnalysisResult]
) -> int:
    """Log all results to Google Sheets. Returns count of rows written."""
    logged = 0
    for result in results:
        if not result.error:
            log_result(client, sheet_id, result)
            logged += 1
    return logged
