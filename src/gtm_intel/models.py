"""Data models for GTM Intel."""

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Company:
    name: str
    url: str
    role: str  # "self" | "competitor" | "partner"


@dataclass
class AnalysisResult:
    company: Company
    mode: str  # "competitive" | "partners" | "self_inspect"
    run_date: str = field(default_factory=lambda: date.today().isoformat())
    core_themes: list[str] = field(default_factory=list)
    context_summary: str = ""
    key_claims: str = ""
    mode_specific: str = ""  # Target Personas / GTM Opportunities / Messaging Gaps
    raw_response: str = ""
    error: str | None = None
