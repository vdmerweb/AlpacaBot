from __future__ import annotations
import logging
from typing import Any, Dict
import requests
from config import Config

logger = logging.getLogger(__name__)

class BrokerException(Exception):
    """Generic broker/connection error for the POC."""
    pass


def get_account(cfg: Config) -> Dict[str, Any]:
    """Retrieve the account object from Alpaca REST API.

    Uses Alpaca REST v2 endpoint `/v2/account`.
    """
    headers = {
        "APCA-API-KEY-ID": cfg.api_key,
        "APCA-API-SECRET-KEY": cfg.secret_key,
    }
    url = cfg.base_url.rstrip("/") + "/v2/account"
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        logger.exception("Failed to fetch account from Alpaca: %s", exc)
        raise BrokerException(str(exc)) from exc
