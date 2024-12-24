import subprocess
import sys
from pathlib import Path
from importlib import import_module
from rich.console import Console
from rich.table import Table

console = Console()

def format_time(duration: float) -> str:
    """
    Convert a duration in seconds to a human-readable string with the appropriate unit.
    Args:
        duration (float): The duration in seconds.
    Returns:
        str: The formatted duration with an appropriate unit.
    """
    if duration < 1e-6:
        return f"{duration * 1e9:.0f} ns"
    elif duration < 1e-3:
        return f"{duration * 1e6:.0f} µs"
    elif duration < 1:
        return f"{duration * 1e3:.01f} ms"
    else:
        return f"{duration:.01f} s"

def run_day(day):
    """Run tests for a given day as well as solutions with both result and performance of each part
        Args:
            day (int): day to run solution for
    """
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
            return

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
            "[red]Ups, you forgot to specify a day to fetch\n(e.g. ./run.py 1)[/red] "
        )
