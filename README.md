# Lint Roller

A tool that automatically lists Pylint rules that are redundant when using ruff.

## Features

- Automatically extracts redundant Pylint rules from ruff's [Implement
  Pylint](https://github.com/astral-sh/ruff/issues/970) issue.
- Generates a `rules.md` file with a list of all of the redundant rules.

# Rules
- The list of the rules is available in [rules.md](rules.md)

## Installation

```bash
git clone https://github.com/ryn-cx/lint-roller.git
cd lint-roller
uv sync
```

## Usage

```bash
uv run lint_roller.py
```
