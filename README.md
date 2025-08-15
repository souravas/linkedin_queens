# linkedin_queens

A small utility that parses a LinkedIn "Queens" puzzle board (saved HTML) and prints a board/solution to the console.

## Requirements

- Python 3.8 or newer

## Run locally

1. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Run the script from the repository root:

```bash
python main.py
```

`main.py` reads `input_html.txt` from the repo root, builds an internal board representation, attempts to place queens, and prints a formatted board to stdout. The script prints a chess queen symbol (♛) for placed queens and color names for empty cells.

## Project layout

- `main.py` — program entry point and puzzle parsing / solving logic.
- `input_html.txt` — sample HTML exported from the LinkedIn Queens game (used as input by `main.py`).
- `LICENSE` — repository license.
- `README.md` — this file.
