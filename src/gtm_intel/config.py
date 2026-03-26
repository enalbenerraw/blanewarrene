"""Configuration loading and validation."""

import sys
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os


@dataclass
class Config:
    gemini_api_key: str
    google_sheets_id: str
    service_account_file: str


def load_config() -> Config:
    """Load configuration from .env file and validate required values."""
    load_dotenv()

    gemini_api_key = os.getenv("GEMINI_API_KEY", "")
    google_sheets_id = os.getenv("GOOGLE_SHEETS_ID", "")
    service_account_file = os.getenv(
        "GOOGLE_SERVICE_ACCOUNT_FILE", "credentials/service-account.json"
    )

    missing = []
    if not gemini_api_key:
        missing.append("GEMINI_API_KEY")
    if not google_sheets_id:
        missing.append("GOOGLE_SHEETS_ID")

    if missing:
        print(f"Missing required environment variables: {', '.join(missing)}")
        print("Copy .env.example to .env and fill in your values.")
        sys.exit(1)

    if not Path(service_account_file).exists():
        print(f"Service account file not found: {service_account_file}")
        print("Download your Google service account JSON and place it in credentials/")
        sys.exit(1)

    return Config(
        gemini_api_key=gemini_api_key,
        google_sheets_id=google_sheets_id,
        service_account_file=service_account_file,
    )
