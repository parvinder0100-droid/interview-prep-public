"""Interactive CLI for PrepIntel powered by Rich."""

import argparse
import sys
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm

from ..parsers import ProgressParser, ReviewParser, NotesParser
from ..analytics import WeaknessEngine, MistakeTaxonomy, ReadinessCalculator
from ..recall import ActiveRecallSession, SpacedScheduler
from .html_generator import generate_html_dashboard
from ..config import OUTPUT_DASHBOARD_HTML

console = Console()

def load_all_data():
    problems = ProgressParser().parse()
    review_parser = ReviewParser()
    reviews = review_parser.parse_schedule()
    review_logs = review_parser.parse_logs()
    notes_parser = NotesParser()
    mistakes = notes_parser.parse_mistake_journal()
    notes_data = notes_parser.parse_notes_invariants()
    return problems, reviews, review_logs, mistakes, notes_data

def cmd_summary(args):
    problems, reviews, review_logs, mistakes, _ = load_all_data()
    calc = ReadinessCalculator(problems, reviews, mistakes)
    profile = calc.calculate_profile()
    weakness_eng = WeaknessEngine(problems, reviews)
    topic_health = weakness_eng.compute_topic_health()

    console.print()
    console.rule("[bold blue]PREPINTEL INTERVIEW PREPARATION COMMAND CENTER[/bold blue]")
    console.print()

    # KPI Grid Panel
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="center", ratio=1)

    readiness_color = "green" if profile.overall_readiness_pct >= 75 else ("yellow" if profile.overall_readiness_pct >= 50 else "red")

    grid.add_row(
        Panel(f"[bold {readiness_color}]{profile.overall_readiness_pct}%[/bold {readiness_color}]\n[dim]FAANG Readiness[/dim]", title="Readiness Index"),
        Panel(f"[bold cyan]{profile.solved_count}/{profile.total_problems}[/bold cyan]\n[dim]{profile.coverage_pct}% Sprint Coverage[/dim]", title="Solved Problems"),
        Panel(f"[bold yellow]{profile.hint_reliance_index}%[/bold yellow]\n[dim]Solves with Hints[/dim]", title="Hint Reliance"),
        Panel(f"[bold red]{profile.total_overdue_reviews}[/bold red]\n[dim]Overdue Reviews[/dim]", title="Review Backlog"),
    )
    console.print(grid)
    console.print()

    # Weaknesses Box
    if profile.top_weaknesses:
        w_text = "\n".join(f"• [bold red]{w}[/bold red]" for w in profile.top_weaknesses)
        console.print(Panel(w_text, title="[bold red]Top Priority Weaknesses & Gaps[/bold red]", border_style="red"))
        console.print()

    # Topic Health Table
    table = Table(title="Topic Health & Fragility Matrix", expand=True)
    table.add_column("Topic", style="bold white")
    table.add_column("Solved / Total", justify="center")
    table.add_column("Hint Debt %", justify="center")
    table.add_column("Overdue", justify="center")
    table.add_column("Health Score", justify="center")
    table.add_column("Status", justify="center")

    for th in topic_health:
        s_color = "green" if th.status == "Solid" else ("yellow" if th.status == "Moderate" else "red")
        table.add_row(
            th.topic,
            f"{th.solved_count} / {th.total_problems}",
            f"{th.hint_reliance_pct}%",
            str(th.overdue_reviews_count),
            f"[{s_color}]{th.health_score}/100[/{s_color}]",
            f"[{s_color}]{th.status}[/{s_color}]"
        )

    console.print(table)
    console.print()
    console.print("[dim]Tip: Run 'python -m prep_intel recall' to drill overdue items or 'python -m prep_intel dashboard' for the web viewer.[/dim]")

def cmd_weaknesses(args):
    problems, reviews, review_logs, mistakes, _ = load_all_data()
    weakness_eng = WeaknessEngine(problems, reviews)
    topic_health = weakness_eng.compute_topic_health()
    risks = weakness_eng.get_highest_risk_problems(limit=12)

    console.print()
    console.rule("[bold red]WEAKNESS & BLINDSPOT DIAGNOSTIC REPORT[/bold red]")
    console.print()

    table = Table(title="Topic Fragility Rankings (Weakest First)", expand=True)
    table.add_column("Rank", justify="center", width=6)
    table.add_column("Topic", style="bold white")
    table.add_column("Health Score", justify="center")
    table.add_column("Hint Debt", justify="center")
    table.add_column("Overdue Reviews", justify="center")
    table.add_column("Diagnosis", style="dim")

    for i, th in enumerate(topic_health, 1):
        s_color = "green" if th.status == "Solid" else ("yellow" if th.status == "Moderate" else "red")
        diag = "Solid retention" if th.status == "Solid" else ("Moderate hint reliance" if th.status == "Moderate" else "Critical: high hints or decay")
        table.add_row(
            str(i),
            th.topic,
            f"[{s_color}]{th.health_score}%[/{s_color}]",
            f"{th.hint_reliance_pct}%",
            str(th.overdue_reviews_count),
            diag
        )
    console.print(table)
    console.print()

    # High-Risk Problems Table
    if risks:
        r_table = Table(title="Top High-Risk Problems (Heavy Hints + Decay)", expand=True)
        r_table.add_column("Problem Name", style="bold white")
        r_table.add_column("Topic", style="cyan")
        r_table.add_column("Risk Profile", style="bold red")
        r_table.add_column("Difficulty", justify="center")

        for p, reason in risks:
            r_table.add_row(p.name, p.topic, reason, p.difficulty)
        console.print(r_table)

def cmd_mistakes(args):
    _, _, _, mistakes, _ = load_all_data()
    tax = MistakeTaxonomy(mistakes)
    cats = tax.get_category_breakdown()

    console.print()
    console.rule("[bold purple]MISTAKE TAXONOMY & ROOT CAUSE ANALYSIS[/bold purple]")
    console.print(f"[dim]Total Logged Mistakes: {len(mistakes)} across all sessions[/dim]\n")

    table = Table(title="Mistake Failure Modes & Preventive Invariants", expand=True)
    table.add_column("Category", style="bold magenta", ratio=2)
    table.add_column("Count", justify="center", ratio=1)
    table.add_column("Share", justify="center", ratio=1)
    table.add_column("Preventive Rule & Invariant", style="italic cyan", ratio=5)

    for cat, cnt, pct, rule in cats:
        table.add_row(cat, str(cnt), f"{pct}%", rule)

    console.print(table)
    console.print()

    # Recent Mistakes Sample
    console.print("[bold]Recent Logged Mistakes (Last 5):[/bold]")
    for m in mistakes[:5]:
        console.print(f"• [bold white]{m.problem}[/bold white] ({m.date}) - [yellow]{m.title}[/yellow]")
        console.print(f"  [dim]Root Cause: {m.root_cause}[/dim]")
        console.print(f"  [green]Rule: {m.how_to_avoid}[/green]\n")

def cmd_recall(args):
    _, reviews, _, _, notes_data = load_all_data()
    session = ActiveRecallSession(reviews, notes_data)
    count = args.count or 5
    cards = session.generate_cards(max_cards=count, priority_only=True)

    console.print()
    console.rule("[bold green]INTERACTIVE ACTIVE RECALL SESSION[/bold green]")
    console.print(f"[dim]Targeting {len(cards)} priority overdue / leech items[/dim]\n")

    if not cards:
        console.print("[green]No reviews due right now! You are completely caught up.[/green]")
        return

    completed_session = []

    for idx, card in enumerate(cards, 1):
        tags_str = " ".join(f"[bold red]{t}[/bold red]" for t in card.tags)
        overdue_str = f"[bold red]{card.days_overdue}d overdue[/bold red]" if card.days_overdue > 0 else "[green]Due today[/green]"

        console.print(Panel(
            f"[bold text-lg]{card.problem_name}[/bold text-lg] (Review #{card.review_num}) {tags_str} • {overdue_str}\n\n"
            f"[bold cyan]Recall Challenge:[/bold cyan]\n{card.question}",
            title=f"Flashcard {idx}/{len(cards)}",
            border_style="blue"
        ))

        Prompt.ask("[dim]Formulate your answer mentally or on scratchpad, then press Enter to reveal invariant[/dim]")

        # Reveal Box
        console.print(Panel(
            f"[bold green]Core Invariant / Optimal Derivation:[/bold green]\n{card.revealed_invariant}\n\n"
            f"[bold red]Known Pitfalls & Historical Traps:[/bold red]\n{card.known_trap if card.known_trap else 'None documented'}",
            title="[bold green]REVEALED ANSWER & MECHANICS[/bold green]",
            border_style="green"
        ))

        choice = Prompt.ask(
            "Self-Assessment Grade",
            choices=["1", "2", "3", "q"],
            default="1"
        )

        if choice == "q":
            console.print("[yellow]Session paused.[/yellow]")
            break

        outcome_map = {"1": "clean", "2": "hint", "3": "fail"}
        outcome = outcome_map[choice]

        next_rev, next_due, grad = SpacedScheduler.calculate_next_interval(card.review_num, outcome)

        completed_session.append((card.problem_name, outcome, next_rev, next_due, grad))

        if grad:
            console.print(f"[bold green]🎉 GRADUATED! {card.problem_name} has cleared 2 clean reviews and exited the ladder![/bold green]\n")
        elif outcome == "clean":
            console.print(f"[green]✓ Clean recall! Advanced to Review #{next_rev} (Next due: {next_due})[/green]\n")
        elif outcome == "hint":
            console.print(f"[yellow]⚡ Guided recall. Review #{next_rev} repeated in 2 days (Next due: {next_due})[/yellow]\n")
        else:
            console.print(f"[red]✗ Lapsed. Reset back to Review #1 (Next due: {next_due})[/red]\n")

    # Session Summary Table
    if completed_session:
        console.rule("[bold blue]ACTIVE RECALL SESSION DEBRIEF[/bold blue]")
        t = Table(expand=True)
        t.add_column("Problem", style="bold white")
        t.add_column("Verdict", justify="center")
        t.add_column("Next Review", justify="center")
        t.add_column("Target Date", justify="center")

        for name, outcome, n_rev, n_due, grad in completed_session:
            o_color = "green" if outcome == "clean" else ("yellow" if outcome == "hint" else "red")
            t.add_row(name, f"[{o_color}]{outcome.upper()}[/{o_color}]", f"#{n_rev}" if not grad else "GRADUATED", n_due)
        console.print(t)
        console.print()

def cmd_dashboard(args):
    problems, reviews, review_logs, mistakes, _ = load_all_data()
    calc = ReadinessCalculator(problems, reviews, mistakes)
    profile = calc.calculate_profile()
    weakness_eng = WeaknessEngine(problems, reviews)
    topic_health = weakness_eng.compute_topic_health()

    out_path = generate_html_dashboard(
        profile=profile,
        topic_health=topic_health,
        problems=problems,
        review_items=reviews,
        mistakes=mistakes
    )

    console.print()
    console.print(f"[bold green]✓ Interactive dashboard successfully generated![/bold green]")
    console.print(f"Path: [cyan]file://{out_path.resolve()}[/cyan]")
    console.print("[dim]Open this file in your browser to view your complete visual telemetry.[/dim]\n")

def main():
    parser = argparse.ArgumentParser(prog="prep_intel", description="PrepIntel Technical Interview Preparation Analytics & Command Center")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command to run")

    subparsers.add_parser("summary", help="Show executive preparation summary & readiness index")
    subparsers.add_parser("weaknesses", help="Show deep-dive weakness & high-risk problems report")
    subparsers.add_parser("mistakes", help="Show categorized mistake taxonomy & preventive rules")
    
    recall_p = subparsers.add_parser("recall", help="Launch interactive active recall terminal session")
    recall_p.add_argument("--count", "-c", type=int, default=5, help="Number of flashcards to drill (default 5)")

    subparsers.add_parser("dashboard", help="Generate and export interactive HTML command center")

    args = parser.parse_args()

    if args.command == "summary":
        cmd_summary(args)
    elif args.command == "weaknesses":
        cmd_weaknesses(args)
    elif args.command == "mistakes":
        cmd_mistakes(args)
    elif args.command == "recall":
        cmd_recall(args)
    elif args.command == "dashboard":
        cmd_dashboard(args)
    else:
        # Default to summary
        cmd_summary(args)

if __name__ == "__main__":
    main()
