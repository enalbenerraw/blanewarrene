"""Claude agent that orchestrates the briefing research and synthesis."""

import anthropic
from app.config import get_settings
from app.prompts.briefing import SYSTEM_PROMPT, BRIEFING_PROMPT
from app.services.tools import TOOL_DEFINITIONS, handle_tool_call


async def generate_briefing(
    company_name: str,
    company_url: str,
    time_period: str = "6 months",
) -> str:
    """Run the full briefing agent loop: Claude researches via tools, then synthesizes."""
    settings = get_settings()
    client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)

    user_message = BRIEFING_PROMPT.format(
        company_name=company_name,
        company_url=company_url,
        time_period=time_period,
    )

    messages = [{"role": "user", "content": user_message}]

    # Agentic loop: Claude calls tools until it produces a final text response
    while True:
        response = await client.messages.create(
            model=settings.claude_model,
            max_tokens=8192,
            system=SYSTEM_PROMPT,
            tools=TOOL_DEFINITIONS,
            messages=messages,
        )

        # If Claude is done (no more tool calls), extract the final text
        if response.stop_reason == "end_turn":
            return _extract_text(response)

        # Process any tool calls in the response
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = await handle_tool_call(block.name, block.input)
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    }
                )

        if not tool_results:
            # No tool calls and not end_turn — return whatever text we have
            return _extract_text(response)

        # Feed tool results back to Claude for the next iteration
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})


async def generate_briefing_stream(
    company_name: str,
    company_url: str,
    time_period: str = "6 months",
):
    """Streaming variant — yields status updates and final content chunks via SSE.

    Yields dicts with:
        {"type": "status", "message": "Searching for..."} during tool calls
        {"type": "content", "text": "..."} for the final briefing text
        {"type": "done"} when complete
    """
    settings = get_settings()
    client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)

    user_message = BRIEFING_PROMPT.format(
        company_name=company_name,
        company_url=company_url,
        time_period=time_period,
    )

    messages = [{"role": "user", "content": user_message}]

    while True:
        response = await client.messages.create(
            model=settings.claude_model,
            max_tokens=8192,
            system=SYSTEM_PROMPT,
            tools=TOOL_DEFINITIONS,
            messages=messages,
        )

        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    yield {"type": "content", "text": block.text}
            yield {"type": "done"}
            return

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                # Send a status update so the iOS app can show progress
                label = _tool_status_label(block.name, block.input)
                yield {"type": "status", "message": label}

                result = await handle_tool_call(block.name, block.input)
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    }
                )

        if not tool_results:
            for block in response.content:
                if hasattr(block, "text"):
                    yield {"type": "content", "text": block.text}
            yield {"type": "done"}
            return

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})


def _extract_text(response) -> str:
    parts = []
    for block in response.content:
        if hasattr(block, "text"):
            parts.append(block.text)
    return "\n".join(parts)


def _tool_status_label(tool_name: str, tool_input: dict) -> str:
    if tool_name == "web_search":
        return f"Searching: {tool_input.get('query', '')[:80]}"
    elif tool_name == "fetch_url":
        return f"Reading: {tool_input.get('url', '')[:80]}"
    return f"Running: {tool_name}"
