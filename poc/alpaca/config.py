from __future__ import annotations
from dataclasses import dataclass
import os
import logging
from typing import Dict

logger = logging.getLogger(__name__)

@dataclass
class Config:
    api_key: str
    secret_key: str
    base_url: str

    @staticmethod
    def _load_dotenv(path: str = ".env") -> Dict[str, str]:
        env: Dict[str, str] = {}
        try:
            with open(path, "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" not in line:
                        continue
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
        except FileNotFoundError:
            logger.debug("No .env file found at %s", path)
        return env

    @classmethod
    def from_env(cls) -> "Config":
        # Prefer environment variables
        api_key = os.getenv("ALPACA_API_KEY") or os.getenv("APCA_API_KEY_ID")
        secret_key = os.getenv("ALPACA_SECRET_KEY") or os.getenv("APCA_API_SECRET_KEY")
        base_url = os.getenv("ALPACA_BASE_URL") or os.getenv("APCA_BASE_URL")

        if not (api_key and secret_key and base_url):
            # Fallback to .env in repository root
            env = cls._load_dotenv()
            api_key = api_key or env.get("ALPACA_API_KEY") or env.get("APCA_API_KEY_ID")
            secret_key = secret_key or env.get("ALPACA_SECRET_KEY") or env.get("APCA_API_SECRET_KEY")
            base_url = base_url or env.get("ALPACA_BASE_URL") or env.get("APCA_BASE_URL")

        missing = [n for n, v in (("ALPACA_API_KEY / APCA_API_KEY_ID", api_key), ("ALPACA_SECRET_KEY / APCA_API_SECRET_KEY", secret_key), ("ALPACA_BASE_URL / APCA_BASE_URL", base_url)) if not v]
        if missing:
            raise ValueError(f"Missing required config values: {', '.join(missing)}")

        return cls(api_key=api_key, secret_key=secret_key, base_url=base_url)
