"""Interactive CLI entry point for GTM Intel."""

import sys

import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from gtm_intel.analyzer import run_analysis
from gtm_intel.auth import validate_gemini, validate_sheets
from gtm_intel.config import load_config
from gtm_intel.models import Company
from gtm_intel.sheets import ensure_tabs, log_results

console = Console()

MODE_CHOICES = [
    questionary.Choice("Competitive Analysis", value="competitive"),
    questionary.Choice("Strategic Partner Analysis", value="partners"),
    questionary.Choice("Self-Inspect", value="self_inspect"),
    questionary.Choice("Run All (batch)", value="all"),
]


def prompt_company(role: str, label: str) -> Company:
    """Prompt for a single company name and URL."""
    name = questionary.text(f"{label} company name:").ask()
    if not name:
        sys.exit(0)
    url = questionary.text(f"{label} website URL:").ask()
    if not url:
        sys.exit(0)
    if not url.startswith("http"):
        url = f"https://{url}"
    return Company(name=name.strip(), url=url.strip(), role=role)


def prompt_company_list(role: str, label: str, required: bool = True) -> list[Company]:
    """Prompt for a list of companies with 'Add another?' loop."""
    companies = []
    while True:
        if not companies and required:
            prompt_label = f"First {label}"
        elif not companies:
            add = questionary.confirm(f"Add a {label}?", default=False).ask()
            if not add:
                return companies
            prompt_label = f"First {label}"
        else:
            add = questionary.confirm(f"Add another {label}?", default=False).ask()
            if not add:
                return companies
            prompt_label = f"Next {label}"

        company = prompt_company(role, prompt_label)
        companies.append(company)
        console.print(f"  Added [bold]{company.name}[/bold]")

    return companies


def prompt_modes() -> list[str]:
    """Prompt user to select which analysis modes to run."""
    selected = questionary.select(
        "Select analysis mode:",
        choices=MODE_CHOICES,
    ).ask()

    if not selected:
        sys.exit(0)

    if selected == "all":
        return ["competitive", "partners", "self_inspect"]
    return [selected]


def display_summary(results: list) -> None:
    """Print a summary table of results to the terminal."""
    table = Table(title="Analysis Summary", show_lines=True)
    table.add_column("Mode", style="bold")
    table.add_column("Company")
    table.add_column("Core Themes")
    table.add_column("Status")

    for r in results:
        if r.error:
            status = f"[red]Error: {r.error[:60]}[/red]"
            themes = ""
        else:
            status = "[green]OK[/green]"
            themes = ", ".join(r.core_themes[:5])
            if len(r.core_themes) > 5:
                themes += f" (+{len(r.core_themes) - 5} more)"

        table.add_row(r.mode, r.company.name, themes, status)

    console.print()
    console.print(table)


def confirm_inputs(
    own_company: Company,
    competitors: list[Company],
    partners: list[Company],
    modes: list[str],
) -> bool:
    """Display a summary and ask for confirmation."""
    console.print()
    console.print(Panel("[bold]Run Summary[/bold]"))
    console.print(f"  Your company: [bold]{own_company.name}[/bold] ({own_company.url})")
    if competitors:
        names = ", ".join(c.name for c in competitors)
        console.print(f"  Competitors:  {names}")
    if partners:
        names = ", ".join(p.name for p in partners)
        console.print(f"  Partners:     {names}")
    console.print(f"  Modes:        {', '.join(modes)}")
    console.print()

    return questionary.confirm("Proceed with analysis?", default=True).ask()


def main() -> None:
    console.print(
        Panel(
            "[bold]GTM Intel[/bold] — Messaging Analysis Tool\n"
            "Analyze competitor, partner, and your own messaging",
            style="blue",
        )
    )

    # Load config and validate APIs
    console.print("[dim]Loading configuration...[/dim]")
    config = load_config()

    console.print("[dim]Validating Gemini API...[/dim]")
    gemini_client = validate_gemini(config)

    console.print("[dim]Validating Google Sheets access...[/dim]")
    sheets_client = validate_sheets(config)

    console.print("[green]Configuration OK[/green]\n")

    # Gather inputs
    console.print(Panel("[bold]Company Setup[/bold]", style="cyan"))

    own_company = prompt_company("self", "Your")
    console.print()

    console.print("[bold]Competitors[/bold]")
    competitors = prompt_company_list("competitor", "competitor", required=True)
    console.print()

    console.print("[bold]Strategic Partners[/bold]")
    partners = prompt_company_list("partner", "partner", required=False)
    console.print()

    # Select modes
    modes = prompt_modes()

    # Validate we have the right inputs for selected modes
    if "partners" in modes and not partners:
        console.print("[yellow]No partners entered — skipping Partner Analysis.[/yellow]")
        modes = [m for m in modes if m != "partners"]

    if not modes:
        console.print("[red]No analysis modes to run. Exiting.[/red]")
        sys.exit(0)

    # Confirm
    if not confirm_inputs(own_company, competitors, partners, modes):
        console.print("Cancelled.")
        sys.exit(0)

    # Ensure spreadsheet tabs exist
    console.print("\n[dim]Setting up spreadsheet tabs...[/dim]")
    ensure_tabs(sheets_client, config.google_sheets_id)

    # Run analyses
    all_results = []
    for mode in modes:
        mode_label = mode.replace("_", " ").title()
        console.print(f"\n[bold blue]Running {mode_label}...[/bold blue]")

        if mode == "competitive":
            targets = competitors
        elif mode == "partners":
            targets = partners
        elif mode == "self_inspect":
            targets = [own_company]
        else:
            continue

        results = run_analysis(gemini_client, mode, targets, own_company)
        all_results.extend(results)

    # Log to Google Sheets
    console.print("\n[dim]Logging results to Google Sheets...[/dim]")
    logged = log_results(sheets_client, config.google_sheets_id, all_results)
    console.print(f"[green]Logged {logged} result(s) to Google Sheets[/green]")

    # Display summary
    display_summary(all_results)
    console.print("\n[bold green]Done![/bold green]")


if __name__ == "__main__":
    main()
