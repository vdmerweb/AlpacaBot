"""Example script showing how to use the safe trade helper.

This script defaults to a dry run to avoid accidental orders. To execute a
paper trade, set `dry_run = False` and ensure your `.env` contains valid
paper API keys.
"""
from trades import safe_place_limit_buy


def main():
    symbol = "AAPL"
    qty = 1
    limit_price = 100.00

    # Keep dry_run=True to avoid placing real orders
    result = safe_place_limit_buy(symbol, qty, limit_price, dry_run=True)
    print("Result:", result)


if __name__ == "__main__":
    main()
