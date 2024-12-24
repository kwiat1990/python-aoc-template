import os
import requests
import sys
from pathlib import Path
from datetime import date
from dotenv import load_dotenv
from rich.console import Console

console = Console()

# Load session cookie from .env
load_dotenv()

SESSION = os.getenv("AOC_SESSION")
YEAR = os.getenv("YEAR") or date.today().year
BASE_URL = "https://adventofcode.com"
TEMPLATE = """def part1(data):
    return None

def part2(data):
    return None

if __name__ == "__main__":
    with open("solutions/day_{:02d}/input.txt") as f:
        data = f.read().strip()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
"""

TEST_TEMPLATE = """import unittest
from solutions.day_{:02d}.solution import part1, part2


class TestDay01(unittest.TestCase):
    sample_input = \"""
...
\"""

    def test_part1(self):
        self.assertEqual(part1(self.sample_input), None)

    def test_part2(self):
        self.assertEqual(part2(self.sample_input), None)
"""


def fetch_input(day):
    if not SESSION:
        raise ValueError("AOC_SESSION not set in .env")

    # Fetch input
    url = f"{BASE_URL}/{YEAR}/day/{day}/input"
    headers = {"Cookie": f"session={SESSION}"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch input for day {day}: {response.status_code}")

    # Save input file
    input_path = Path(f"solutions/day_{day:02d}/input.txt")
    input_path.parent.mkdir(exist_ok=True)
    input_path.write_text(response.text.strip())
    console.print(f"Input saved to {input_path}")

    # Create solution file
    solution_path = Path(f"solutions/day_{day:02d}/solution.py")
    if not solution_path.exists():
        solution_path.write_text(TEMPLATE.format(day))
        console.print(f"Solution template created: {solution_path}")

    # Create test file
    test_path = Path(f"solutions/day_{day:02d}/test_solution.py")
    if not test_path.exists():
        test_path.write_text(TEST_TEMPLATE.format(day))
        console.print(f"Test template created: {test_path}")

    # Create init file to treat it as module
    test_path = Path(f"solutions/day_{day:02d}/__init__.py")
    if not test_path.exists():
        test_path.write_text("")


if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
        fetch_input(day)
    except IndexError:
        console.print(
            "[red]Oopla, you forgot to specify a day to fetch\n(e.g. ./fetch.py 1)[/red] "
        )
