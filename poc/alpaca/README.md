POC-001 — Alpaca Authentication & Account Retrieval

Purpose

This POC validates connectivity to the Alpaca Paper Trading REST API and retrieves account information.

Quick start

1. Add your Alpaca credentials to a `.env` file at the repository root (do not commit):

```
ALPACA_API_KEY=YOUR_KEY
ALPACA_SECRET_KEY=YOUR_SECRET
ALPACA_BASE_URL=https://paper-api.alpaca.markets
```

Alternative supported names for the POC:

```
APCA_API_KEY_ID=YOUR_KEY
APCA_API_SECRET_KEY=YOUR_SECRET
APCA_BASE_URL=https://paper-api.alpaca.markets
```

2. Create a virtual environment and install requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r poc/alpaca/requirements.txt
```

3. Run the POC:

```powershell
python poc\alpaca\main.py
```

Notes

- This is a POC. Do not treat its structure as the final architecture.
- The Implementation Engineer should capture lessons learned in `docs/steering/PROJECT_CONTEXT.md` under "Learning Log".
