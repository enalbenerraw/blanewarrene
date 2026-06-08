from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    anthropic_api_key: str
    brave_search_api_key: str
    database_url: str = "postgresql+asyncpg://user:pass@localhost:5432/signalwatch"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 60 * 24 * 7  # 1 week

    # One-time passcode (magic link / email OTP) config
    otp_length: int = 6
    otp_expiration_minutes: int = 10

    # Email transport. When smtp_host is unset, OTP codes are written to the
    # application log instead of sent (dev mode), so the flow is testable
    # without a provider configured.
    smtp_host: str | None = None
    smtp_port: int = 587
    smtp_username: str | None = None
    smtp_password: str | None = None
    smtp_from: str = "Signal Watch <no-reply@signalwatch.app>"
    smtp_use_tls: bool = True

    # Claude model config
    claude_model: str = "claude-sonnet-4-20250514"
    max_search_results: int = 10

    model_config = {"env_file": ".env"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
