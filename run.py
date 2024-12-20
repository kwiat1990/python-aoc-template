import subprocess
import sys
from pathlib import Path
from importlib import import_module
from rich.console import Console
from rich.table import Table

console = Console()


def run_day(day):
    try:
        # Run the tests for the day
        console.print(f"Running tests for Day {day}...")
        result = subprocess.run(
            ["python", "-m", "unittest", f"solutions/day_{day:02d}/test_solution.py"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            console.print("[green bold]✔ All tests passed![/green bold]")
        else:
            console.print("[red bold]✘ Tests failed:[/red bold]")
            console.print(result.stderr)

        # Run the solution
        console.print(f"Running solution for Day {day}...")
        input_file = Path(f"solutions/day_{day:02d}/input.txt")
        if not input_file.exists():
            console.print(f"[red]Input for day {day} not found![/red]")
            return

        data = input_file.read_text().strip()
        module = import_module(f"solutions.day_{day:02d}.solution")
        part1 = module.part1(data)
        part2 = module.part2(data)

        table = Table(title=f"Day {day} Results")
        table.add_column("Part", justify="right", style="cyan", no_wrap=True)
        table.add_column("Result", style="green")
        table.add_row("Part 1", str(part1))
        table.add_row("Part 2", str(part2))
        console.print(table)

    except ModuleNotFoundError:
        console.print(f"[red]Solution for day {day} not found![/red]")
    except Exception as e:
        console.print(f"[red]Error while running day {day}: {e}[/red]")


if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
        run_day(day)
    except IndexError:
        console.print(
            "[red]Oopla, you forgot to specify a day to fetch\n(e.g. ./run.py 1)[/red] "
        )
