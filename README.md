# Lint Roller

A tool that automatically disables Pylint rules that are redundant when using Ruff.

## Overview

Lint Roller helps you maintain a clean and efficient linting setup by automatically disabling Pylint rules that are already covered by Ruff. This prevents duplicate warnings and keeps your linting configuration focused on what matters.

## Features

- Automatically extracts redundant Pylint rules from Ruff's compatibility list
- Generates a `.pylintrc` configuration file with the appropriate rules disabled
- Maintains a clean and efficient linting setup
- Compatible with Python 3.13+

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

The tool will:
1. Extract the redundant Pylint rules from the input file
2. Generate a `.pylintrc` configuration file with these rules disabled
3. Keep all other Pylint configurations at their default values

## Requirements

- Python 3.13 or higher
