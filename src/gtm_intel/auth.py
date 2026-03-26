"""Authentication helpers for Gemini and Google Sheets APIs."""

from google import genai
import gspread
from google.oauth2.service_account import Credentials

from gtm_intel.config import Config

SHEETS_SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def validate_gemini(config: Config) -> genai.Client:
    """Configure Gemini API and return a client."""
    client = genai.Client(api_key=config.gemini_api_key)
    try:
        client.models.list()
    except Exception as e:
        raise RuntimeError(f"Gemini API key validation failed: {e}") from e
    return client


def validate_sheets(config: Config) -> gspread.Client:
    """Authenticate with Google Sheets and verify access to the target spreadsheet."""
    creds = Credentials.from_service_account_file(
        config.service_account_file, scopes=SHEETS_SCOPES
    )
    client = gspread.authorize(creds)
    try:
        client.open_by_key(config.google_sheets_id)
    except gspread.SpreadsheetNotFound:
        raise RuntimeError(
            f"Cannot access spreadsheet {config.google_sheets_id}. "
            "Make sure you've shared it with the service account email."
        )
    return client
