from typing import Any


def place_limit_buy(client: Any, symbol: str, qty: int, limit_price: float) -> Any:
    """Place a limit buy order using the provided Alpaca TradingClient-like object.

    This function is client-agnostic and is safe to unit-test by passing a mock
    object that implements `submit_order`.
    """
    if qty <= 0:
        raise ValueError("qty must be > 0")
    if limit_price <= 0:
        raise ValueError("limit_price must be > 0")

    # The alpaca-py client uses `submit_order` for submitting orders.
    order = client.submit_order(
        symbol=symbol,
        qty=qty,
        side="buy",
        type="limit",
        time_in_force="gtc",
        limit_price=limit_price,
    )

    return order


def safe_place_limit_buy(symbol: str, qty: int, limit_price: float, dry_run: bool = True) -> Any:
    """High-level helper that performs a dry-run by default.

    If `dry_run` is False it will create a real TradingClient from `config` and
    place the order on the Alpaca paper API. Keep `dry_run=True` unless you
    intentionally want to execute a paper trade.
    """
    if dry_run:
        return {"status": "dry_run", "symbol": symbol, "qty": qty, "limit_price": limit_price}

    from alpaca.trading.client import TradingClient
    from config import API_KEY, SECRET_KEY

    if not API_KEY or not SECRET_KEY:
        raise RuntimeError("API credentials not configured")

    client = TradingClient(api_key=API_KEY, secret_key=SECRET_KEY, paper=True)
    return place_limit_buy(client, symbol, qty, limit_price)
