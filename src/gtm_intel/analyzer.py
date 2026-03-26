"""Core analysis engine — calls Gemini with grounding and parses responses."""

import json
import re
import time

from google import genai
from google.genai import types
from rich.console import Console

from gtm_intel.models import AnalysisResult, Company
from gtm_intel.prompts import build_prompt

console = Console()


def parse_response(text: str) -> dict:
    """Extract JSON from Gemini's response, handling markdown fences."""
    cleaned = text.strip()
    # Strip markdown JSON fences if present
    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(1).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "core_themes": [],
            "context_summary": text[:2000],
            "key_claims": "",
            "mode_specific": "",
            "raw_narrative": text,
        }


def run_single_analysis(
    client: genai.Client,
    mode: str,
    company: Company,
    own_company: Company,
) -> AnalysisResult:
    """Run analysis for a single company in a given mode."""
    prompt = build_prompt(mode, company, own_company)

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
            ),
        )
        parsed = parse_response(response.text)

        return AnalysisResult(
            company=company,
            mode=mode,
            core_themes=parsed.get("core_themes", []),
            context_summary=parsed.get("context_summary", ""),
            key_claims=parsed.get("key_claims", ""),
            mode_specific=parsed.get("mode_specific", ""),
            raw_response=parsed.get("raw_narrative", response.text),
        )
    except Exception as e:
        return AnalysisResult(
            company=company,
            mode=mode,
            error=str(e),
            context_summary=f"Analysis failed: {e}",
        )


def run_analysis(
    client: genai.Client,
    mode: str,
    companies: list[Company],
    own_company: Company,
    delay: float = 2.0,
) -> list[AnalysisResult]:
    """Run analysis for all companies in a given mode."""
    results = []
    for i, company in enumerate(companies):
        label = company.name if mode != "self_inspect" else own_company.name
        console.print(f"  Analyzing [bold]{label}[/bold]...")

        result = run_single_analysis(client, mode, company, own_company)
        results.append(result)

        if result.error:
            console.print(f"  [red]Error: {result.error}[/red]")
        else:
            console.print(f"  [green]Done[/green] — {len(result.core_themes)} themes found")

        # Rate limit buffer between API calls
        if i < len(companies) - 1:
            time.sleep(delay)

    return results
