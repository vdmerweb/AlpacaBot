"""POC-001: Alpaca authentication and account retrieval

Run: python main.py

This is intentionally a simple, standalone POC. It is not production code.
"""
from __future__ import annotations
import logging
import sys
from config import Config
from account_service import get_account, BrokerException

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("poc.alpaca")


def print_account_summary(account: dict) -> None:
    # Keys may vary depending on Alpaca's API version - use .get() defensively
    print("Account Number:", account.get("id") or account.get("account_number") or "(unknown)")
    print("Status:", account.get("status", "(unknown)"))
    print("Currency:", account.get("currency", "USD"))
    print("Buying Power:", account.get("buying_power", "(unknown)"))
    print("Cash:", account.get("cash", "(unknown)"))
    print("Portfolio Value:", account.get("portfolio_value", account.get("equity", "(unknown)")))


def main() -> int:
    try:
        cfg = Config.from_env()
    except ValueError as exc:
        logger.error("Configuration error: %s", exc)
        return 2

    logger.info("Connecting to Alpaca at %s", cfg.base_url)
    try:
        account = get_account(cfg)
    except BrokerException as exc:
        logger.error("Failed to retrieve account: %s", exc)
        return 3

    print_account_summary(account)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
