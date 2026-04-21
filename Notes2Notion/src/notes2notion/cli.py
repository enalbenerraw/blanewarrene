"""Notes2Notion CLI — interactive and batch Apple Notes to Notion export."""

import argparse
import sys
from pathlib import Path

import questionary
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.table import Table

from . import applescript
from .extractor import discover_folders, extract_notes
from .models import ExportConfig
from .writer import write_export

console = Console()


def _check_platform():
    if sys.platform != "darwin":
        console.print(
            "[red bold]Error:[/] Notes2Notion requires macOS "
            "(Apple Notes is not available on this platform)."
        )
        sys.exit(1)


def _check_notes_access():
    console.print("Connecting to Notes.app...", end=" ")
    if not applescript.check_access():
        console.print("[red]FAILED[/]")
        console.print(
            "\n[red bold]Error:[/] Cannot access Notes.app. "
            "Please grant Terminal/IDE access in "
            "System Settings > Privacy & Security > Automation."
        )
        sys.exit(1)
    console.print("[green]OK[/]")


def _select_folders(folders) -> list[str] | None:
    """Interactive folder selection. Returns None for 'all'."""
    choices = [
        questionary.Choice("All Notes", value="__all__"),
    ] + [
        questionary.Choice(f"{f.name} ({f.note_count} notes)", value=f.name)
        for f in folders
    ]

    selected = questionary.checkbox(
        "Select folders to export:",
        choices=choices,
    ).ask()

    if selected is None:
        console.print("[yellow]Export cancelled.[/]")
        sys.exit(0)

    if "__all__" in selected:
        return None

    if not selected:
        console.print("[yellow]No folders selected. Exiting.[/]")
        sys.exit(0)

    return selected


def _select_date_range() -> int | None:
    """Interactive date-range selection. Returns days-back window, or None for all."""
    # Use a string sentinel for "all" so we can distinguish that choice from
    # a Ctrl-C abort (which questionary signals by returning None).
    choice = questionary.select(
        "Include notes created within:",
        choices=[
            questionary.Choice("All time (no filter)", value="all"),
            questionary.Choice("Last 30 days", value=30),
            questionary.Choice("Last 90 days", value=90),
            questionary.Choice("Last 180 days", value=180),
        ],
        default="all",
    ).ask()

    if choice is None:
        console.print("[yellow]Export cancelled.[/]")
        sys.exit(0)

    return None if choice == "all" else choice


def _get_output_dir() -> Path:
    """Prompt for the output directory."""
    default = str(Path.home() / "Desktop" / "notes2notion_export")
    path_str = questionary.text(
        "Output directory:",
        default=default,
    ).ask()

    if path_str is None:
        console.print("[yellow]Export cancelled.[/]")
        sys.exit(0)

    return Path(path_str).expanduser().resolve()


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export Apple Notes to Notion-importable Markdown"
    )
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Run in non-interactive batch mode (no prompts)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        dest="all_folders",
        help="Export all folders (batch mode)",
    )
    parser.add_argument(
        "--folders",
        type=str,
        default=None,
        help="Comma-separated folder names to export (batch mode)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output directory path (batch mode)",
    )
    parser.add_argument(
        "--last-days",
        type=int,
        choices=[30, 90, 180],
        default=None,
        help="Only export notes created within the last N days (30, 90, or 180)",
    )
    return parser.parse_args()


def _run_batch(args: argparse.Namespace):
    """Run export in non-interactive batch mode."""
    _check_platform()
    _check_notes_access()

    folders = discover_folders()
    if not folders:
        console.print("[yellow]No folders found in Notes.app.[/]")
        sys.exit(1)

    # Determine folder selection
    if args.folders:
        selected_folders = [f.strip() for f in args.folders.split(",")]
        available = {f.name for f in folders}
        invalid = [f for f in selected_folders if f not in available]
        if invalid:
            console.print(f"[red]Error:[/] Unknown folders: {', '.join(invalid)}")
            console.print(f"Available: {', '.join(sorted(available))}")
            sys.exit(1)
    else:
        selected_folders = None  # all folders

    # Determine output directory
    if args.output:
        output_dir = Path(args.output).expanduser().resolve()
    else:
        output_dir = Path.home() / "Desktop" / "notes2notion_export"

    if selected_folders is None:
        total = sum(f.note_count for f in folders)
    else:
        total = sum(f.note_count for f in folders if f.name in selected_folders)

    date_note = f" (created within last {args.last_days} days)" if args.last_days else ""
    console.print(f"Exporting up to {total} notes{date_note} to {output_dir}")

    config = ExportConfig(
        output_dir=output_dir,
        folders=selected_folders,
        created_within_days=args.last_days,
    )
    warnings: list[str] = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        console=console,
    ) as progress:
        task = progress.add_task("Exporting notes...", total=total)

        def on_progress(name: str, current: int, total: int):
            progress.update(task, completed=current, description=f"Exporting: {name[:40]}")

        def on_warning(msg: str):
            warnings.append(msg)

        notes = extract_notes(config, on_progress=on_progress, on_warning=on_warning)

    out_dir, zip_path, write_warnings = write_export(notes, output_dir, create_zip=True)
    warnings.extend(write_warnings)

    attachment_count = sum(len(n.attachments) for n in notes)
    skipped_count = total - len(notes)

    # Print machine-parseable summary for the AppleScript app
    console.print(f"\nNotes exported: {len(notes)}")
    console.print(f"Attachments: {attachment_count}")
    console.print(f"Skipped: {skipped_count}")
    console.print(f"Output: {out_dir}")
    if zip_path:
        console.print(f"ZIP: {zip_path}")

    if warnings:
        for w in warnings:
            console.print(f"Warning: {w}", style="yellow")

    sys.exit(0)


def main():
    """Entry point for Notes2Notion CLI."""
    args = _parse_args()

    if args.batch:
        _run_batch(args)
        return

    # Interactive mode
    console.print(
        Panel(
            "[bold]Notes2Notion[/] — Apple Notes to Notion Export",
            expand=False,
        )
    )
    console.print()

    _check_platform()
    _check_notes_access()
    console.print()

    # Discover folders
    folders = discover_folders()
    if not folders:
        console.print("[yellow]No folders found in Notes.app.[/]")
        sys.exit(0)

    # Show folder summary
    folder_table = Table(title="Apple Notes Folders")
    folder_table.add_column("Folder", style="cyan")
    folder_table.add_column("Notes", justify="right")
    for f in folders:
        folder_table.add_row(f.name, str(f.note_count))
    console.print(folder_table)
    console.print()

    # Select folders
    selected_folders = _select_folders(folders)

    # Date range filter (optional)
    created_within_days = _select_date_range()

    if selected_folders is None:
        total = sum(f.note_count for f in folders)
        folder_label = "all folders"
    else:
        total = sum(
            f.note_count for f in folders if f.name in selected_folders
        )
        folder_label = ", ".join(selected_folders)

    date_label = (
        f", created within last {created_within_days} days"
        if created_within_days else ""
    )
    console.print(
        f"\nFound [bold]{total}[/] notes in {folder_label}{date_label}."
    )

    # Confirm
    if not questionary.confirm("Proceed with export?", default=True).ask():
        console.print("[yellow]Export cancelled.[/]")
        sys.exit(0)

    # Output directory
    output_dir = _get_output_dir()

    # Extract notes with progress
    config = ExportConfig(
        output_dir=output_dir,
        folders=selected_folders,
        created_within_days=created_within_days,
    )

    warnings: list[str] = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        console=console,
    ) as progress:
        task = progress.add_task("Exporting notes...", total=total)

        def on_progress(name: str, current: int, total: int):
            progress.update(task, completed=current, description=f"Exporting: {name[:40]}")

        def on_warning(msg: str):
            warnings.append(msg)

        notes = extract_notes(
            config,
            on_progress=on_progress,
            on_warning=on_warning,
        )

    console.print()

    # Write output
    with console.status("Writing files and creating ZIP..."):
        out_dir, zip_path, write_warnings = write_export(
            notes, output_dir, create_zip=True
        )
        warnings.extend(write_warnings)

    # Summary
    attachment_count = sum(len(n.attachments) for n in notes)
    skipped_count = total - len(notes)

    summary = Table(title="Export Complete", show_header=False, box=None)
    summary.add_column(style="bold")
    summary.add_column()
    summary.add_row("Notes exported:", str(len(notes)))
    summary.add_row("Attachments:", str(attachment_count))
    if created_within_days:
        summary.add_row("Date filter:", f"last {created_within_days} days")
    if skipped_count > 0:
        label = "Skipped or filtered:" if created_within_days else "Skipped:"
        summary.add_row(label, f"[yellow]{skipped_count}[/]")
    summary.add_row("Output:", str(out_dir))
    if zip_path:
        summary.add_row("ZIP:", str(zip_path))

    console.print(Panel(summary, expand=False))

    # Show warnings
    if warnings:
        console.print("\n[yellow bold]Warnings:[/]")
        for w in warnings:
            console.print(f"  [yellow]- {w}[/]")

    # Import instructions
    console.print("\n[bold]To import into Notion:[/]")
    console.print("  1. Open Notion > Settings > Import")
    console.print('  2. Select "Markdown & CSV"')
    if zip_path:
        console.print(f"  3. Upload [cyan]{zip_path.name}[/]")
    else:
        console.print(f"  3. Upload the files from [cyan]{out_dir}[/]")
    console.print()
