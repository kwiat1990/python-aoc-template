# Advent of Code Template

This repository contains my solutions for [Advent of Code](https://adventofcode.com/).

## Progress

|Day|Part 1 ⭐|Part 2 ⭐|Solutions| Notes|
|:-:|:-:|:-:|:-:|-|
|1|⭐|⭐| [Solution](solutions/day_01/solution.py)|Great day!|
|2| | | | |
|3| | | | |
|4| | | | |
|5| | | | |
|6| | | | |
|7| | | | |
|8| | | | |
|9| | | | |
|10| | | | |
|11| | | | |
|12| | | | |
|13| | | | |
|14| | | | |
|15| | | | |
|16| | | | |
|17| | | | |
|18| | | | |
|19| | | | |
|20| | | | |
|21| | | | |
|22| | | | |
|23| | | | |
|24| | | | |
|25| | | | |

Total Stars: 🌟 0 / 50

## Project Structure

```
root 
|__fetch.py
|__run.py
|__requirements.txt
|__solutions
   |__day_<01..25>
      |__input.txt
      |__solution.py
      |__test_solution.py
      |____init__.py
```

## Setting Up
### Install Dependencies:
```bash
pip install -r requirements.txt
```
### Activate Virtual Environment (optional)
```bash
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

## Fetching and running solution for a given day

### Ensure ENV Variable are set

Add your session cookie from the Advent of Code website to a .env file:

```bash
AOC_SESSION=<your-session-cookie>
YEAR=<optional-fallback-to-current-year>
```
### Fetching Input
Use `fetch.py` to download the puzzle input for a specific day.

Run `fetch.py`:
```bash
python fetch.py <day>
```
Replace <day> with the day number (e.g., 1 for Day 1). 

**The script will**:
* Fetch the input for the specified day.
* Save it to `solutions/day_<day>/input.txt`.

### Running Solutions
Use `run.py` to execute solutions for a specific day and replace <day> with the day number:

```bash
python run.py <day>
````

**The script will:**
* Import the part1 and part2 functions from `solutions/day_<day>/solution.py`.
* Read the input.txt file for that day.
* Run tests for that day.
* Print the results for both parts.

### Running Tests
Each day includes unit tests to verify the solutions for both parts.

Run All Tests:
```bash
python -m unittest discover -s solutions -p "test_*.py"`
```

Run Tests for a Specific Day:
```bash
python -m unittest solutions/day_01/test_solution.py
```


