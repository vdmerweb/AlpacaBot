# Project Status

## Current State
- The project connects to Alpaca paper trading using local credentials in `.env`.
- `.env` is listed in `.gitignore` and is not tracked by git.
- `config.py` loads API keys from environment variables and does not contain hardcoded secrets.
- `main.py` now validates credentials and connects to the Alpaca paper account.
- Local tests run successfully with `pytest -q`.

## Dependencies
- `alpaca-py`
- `python-dotenv`
- `pytest`

## Local example and tests
- `examples/safe_trade.py` provides a dry-run example for placing a paper order.
- `trades.py` contains a safe helper: `safe_place_limit_buy(..., dry_run=True)`.
- `tests/test_trades.py` uses mocks and pytest to validate trade helper behavior.
- `tests/conftest.py` adds the project root to `sys.path` so tests can import local modules.

## Pre-commit / pre-push workflow
- `.pre-commit-config.yaml` is configured with two local hooks for the `push` stage:
  - `check-env-ignored`: ensures `.env` is ignored by git.
  - `run-pytest`: runs `pytest -q`.
- Current configuration also includes `check-added-large-files` from `pre-commit-hooks`.
- The git hook is not automatically installed by default; run `pre-commit install --hook-type pre-push` to enable automatic checks on `git push`.

## CI workflow
- `.github/workflows/ci.yml` runs on `push` and `pull_request` targeting `main`.
- The CI job installs dependencies, installs `pre-commit`, runs `pre-commit run --all-files`, and then runs `pytest -q`.

## Recommended next step
1. Install pre-commit locally: `pip install pre-commit`
2. Enable the pre-push hook: `pre-commit install --hook-type pre-push`
3. Run the checks manually if needed: `pre-commit run --all-files` or `pre-commit run --hook-stage push`

## Notes
- Secrets are safe as long as `.env` remains untracked and not committed.
- If secrets were ever committed, rotate them and remove them from repo history.
