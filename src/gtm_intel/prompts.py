"""Prompt templates for each analysis mode."""

from gtm_intel.models import Company

JSON_INSTRUCTION = """
Return your analysis as JSON with these exact keys:
{
  "core_themes": ["theme1", "theme2", ...],
  "context_summary": "2-3 paragraph summary of the messaging analysis",
  "key_claims": "specific claims found in paid and organic content",
  "mode_specific": "see specific instruction below",
  "raw_narrative": "full detailed analysis with all findings"
}

IMPORTANT: Return ONLY the JSON object, no markdown fencing or extra text.
"""


def build_competitive_prompt(competitor: Company, own_company: Company) -> str:
    return f"""You are a Senior Competitive Intelligence Analyst. Analyze the public messaging
of {competitor.name} ({competitor.url}) over the past 7 days.

Search for and analyze:
1. PAID CONTENT: Google ads, LinkedIn sponsored posts, Facebook/Meta ads, X promoted posts
   from {competitor.name} in the last 7 days.
2. ORGANIC CONTENT: Blog posts, product updates, press releases, and social media posts
   (LinkedIn, X) from {competitor.name} in the last 7 days.
3. WEBSITE: Current homepage and key landing page messaging on {competitor.url}.

From this research, extract:
- Core messaging themes and narratives being pushed
- Key claims being made about their product or service
- Target personas and pain points being addressed
- Competitive positioning — how they differentiate themselves
- Any new campaigns, launches, or partnerships highlighted

Context: I work at {own_company.name} ({own_company.url}) and need to understand
what {competitor.name} is saying in the market right now.

For the "mode_specific" field, provide the target personas and audience segments
this messaging appears aimed at.

If you cannot find content from the last 7 days, note what timeframe you were able
to find and flag the gap. Do not fabricate content.

{JSON_INSTRUCTION}"""


def build_partner_prompt(partner: Company, own_company: Company) -> str:
    return f"""You are a Senior Competitive Intelligence Analyst focused on strategic partnerships.
Analyze the public messaging of {partner.name} ({partner.url}) over the past 7 days.

Search for and analyze:
1. PAID CONTENT: Google ads, LinkedIn sponsored posts, Facebook/Meta ads, X promoted posts
   from {partner.name} in the last 7 days.
2. ORGANIC CONTENT: Blog posts, product updates, press releases, and social media posts
   (LinkedIn, X) from {partner.name} in the last 7 days.
3. WEBSITE: Current homepage and key landing page messaging on {partner.url}.

From this research, extract:
- Core messaging themes and narratives being pushed
- Key claims being made about their product or service
- Campaigns, launches, or partnerships being highlighted
- How they are positioning their ecosystem and partner relationships

Context: I work at {own_company.name} ({own_company.url}) and {partner.name} is one of
our strategic partners. I need to understand their current messaging so we can align
our go-to-market activity.

For the "mode_specific" field, identify specific posts, campaigns, or themes from
{partner.name} that {own_company.name} could interact with, amplify, co-market with,
or respond to via our own paid and organic GTM activity. Be specific about which
content and what the interaction strategy would be.

If you cannot find content from the last 7 days, note what timeframe you were able
to find and flag the gap. Do not fabricate content.

{JSON_INSTRUCTION}"""


def build_self_inspect_prompt(own_company: Company) -> str:
    return f"""You are a Senior Competitive Intelligence Analyst performing a self-audit.
Analyze the public messaging of {own_company.name} ({own_company.url}) over the past 7 days.

Search for and analyze:
1. PAID CONTENT: Google ads, LinkedIn sponsored posts, Facebook/Meta ads, X promoted posts
   from {own_company.name} in the last 7 days.
2. ORGANIC CONTENT: Blog posts, product updates, press releases, and social media posts
   (LinkedIn, X) from {own_company.name} in the last 7 days.
3. WEBSITE: Current homepage and key landing page messaging on {own_company.url}.

From this research, extract:
- Core messaging themes and narratives we are pushing
- Key claims we are making about our product or service
- Target personas and pain points we are addressing
- How consistent our messaging is across channels
- Any gaps between what we say on our website vs. social vs. ads

For the "mode_specific" field, identify messaging gaps or drift — areas where our
messaging is inconsistent, unclear, or missing compared to what we could be saying.
Note any themes competitors might be exploiting that we are not addressing.

If you cannot find content from the last 7 days, note what timeframe you were able
to find and flag the gap. Do not fabricate content.

{JSON_INSTRUCTION}"""


def build_prompt(mode: str, company: Company, own_company: Company) -> str:
    if mode == "competitive":
        return build_competitive_prompt(company, own_company)
    elif mode == "partners":
        return build_partner_prompt(company, own_company)
    elif mode == "self_inspect":
        return build_self_inspect_prompt(own_company)
    else:
        raise ValueError(f"Unknown mode: {mode}")
