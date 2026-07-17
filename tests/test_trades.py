import pytest
from unittest.mock import Mock

from trades import place_limit_buy, safe_place_limit_buy


def test_place_limit_buy_calls_submit_order():
    mock_client = Mock()
    mock_client.submit_order.return_value = {"id": "order123"}

    res = place_limit_buy(mock_client, "AAPL", 1, 100.0)

    mock_client.submit_order.assert_called_once_with(
        symbol="AAPL",
        qty=1,
        side="buy",
        type="limit",
        time_in_force="gtc",
        limit_price=100.0,
    )
    assert res == {"id": "order123"}


def test_place_limit_buy_invalid_values():
    mock_client = Mock()
    with pytest.raises(ValueError):
        place_limit_buy(mock_client, "AAPL", 0, 100.0)
    with pytest.raises(ValueError):
        place_limit_buy(mock_client, "AAPL", 1, -10.0)


def test_safe_place_limit_buy_dry_run():
    res = safe_place_limit_buy("AAPL", 1, 100.0, dry_run=True)
    assert res["status"] == "dry_run"
    assert res["symbol"] == "AAPL"
