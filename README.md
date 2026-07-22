# AlpacaBot

[![CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml/badge.svg)](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml)

A small Alpaca paper trading example project.

## What it does
- Connects to Alpaca paper trading using `alpaca-py`.
- Loads credentials from a local `.env` file using `python-dotenv`.
- Includes a safe dry-run example trade and unit tests.
- Includes a GitHub Actions CI workflow for tests and pre-commit checks.

## Files of interest
- `main.py` — connects to Alpaca and prints account information.
- `config.py` — loads credentials from environment variables.
- `trades.py` — safe trade helper functions.
- `examples/safe_trade.py` — example dry-run limit buy.
- `tests/test_trades.py` — pytest tests for trading helpers.
- `PROJECT_STATUS.md` — current project status and safety notes.
- `docs/architecture/README.md` — architecture document index.
- `docs/architecture/EXECUTIVE_ARCHITECTURE_SUMMARY_v1.md` — north-star architecture summary.
- `docs/architecture/PHASE_2_ARCHITECTURE_BASELINE_v1.md` — Architecture Baseline v1.0 roadmap.
- `.github/workflows/ci.yml` — CI workflow for GitHub Actions.
- `.pre-commit-config.yaml` — local hooks for pre-push checks.

## Setup
1. Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Copy the example env file and add your Alpaca paper keys:

```powershell
Copy-Item .env.example .env
notepad .env
```

4. Confirm `.env` is ignored:

```powershell
git check-ignore -v .env
```

## Running the app

```powershell
python main.py
```

## Example dry-run trade

```powershell
python examples/safe_trade.py
```

## Tests

```powershell
pytest -q
```

## Pre-push safety checks

Install pre-commit and enable the pre-push hook:

```powershell
pip install pre-commit
pre-commit install --hook-type pre-push
```

Then the pre-push hook will run:
- `.env` ignored check
- `pytest -q`

You can also run all checks manually:

```powershell
pre-commit run --all-files
```

## CI

GitHub Actions runs on `push` and `pull_request` to `main` and performs:
- dependency install
- `pre-commit run --all-files`
- `pytest -q`

## Secrets safety
- Do not commit `.env`.
- Store your Alpaca keys only in `.env` or session environment variables.
- If a secret is accidentally committed, rotate it immediately.
