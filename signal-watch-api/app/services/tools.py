"""Web research tools that Claude calls via tool_use during briefing generation."""

import httpx
from app.config import get_settings

# Tool definitions sent to the Claude API
TOOL_DEFINITIONS = [
    {
        "name": "web_search",
        "description": (
            "Search the web for current information about a company, person, or topic. "
            "Returns a list of search results with titles, URLs, and snippets."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "fetch_url",
        "description": (
            "Fetch the text content of a web page. Use this to read company websites, "
            "newsrooms, blog posts, press releases, and other public pages."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL to fetch",
                },
            },
            "required": ["url"],
        },
    },
]


async def handle_tool_call(tool_name: str, tool_input: dict) -> str:
    """Execute a tool call from Claude and return the result as text."""
    if tool_name == "web_search":
        return await _web_search(tool_input["query"])
    elif tool_name == "fetch_url":
        return await _fetch_url(tool_input["url"])
    else:
        return f"Unknown tool: {tool_name}"


async def _web_search(query: str) -> str:
    """Search using Brave Search API."""
    settings = get_settings()
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://api.search.brave.com/res/v1/web/search",
            headers={
                "Accept": "application/json",
                "Accept-Encoding": "gzip",
                "X-Subscription-Token": settings.brave_search_api_key,
            },
            params={"q": query, "count": settings.max_search_results},
            timeout=15.0,
        )
        resp.raise_for_status()
        data = resp.json()

    results = data.get("web", {}).get("results", [])
    if not results:
        return "No search results found."

    lines = []
    for r in results:
        lines.append(f"**{r['title']}**\n{r['url']}\n{r.get('description', '')}\n")
    return "\n".join(lines)


async def _fetch_url(url: str) -> str:
    """Fetch and return the text content of a URL, truncated to avoid token blowup."""
    max_chars = 15_000
    async with httpx.AsyncClient(follow_redirects=True) as client:
        resp = await client.get(
            url,
            headers={"User-Agent": "SignalWatch/1.0 (research bot)"},
            timeout=15.0,
        )
        resp.raise_for_status()
        text = resp.text[:max_chars]
    return text
