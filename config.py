import os
from dotenv import load_dotenv

load_dotenv()

# Read Alpaca credentials from environment variables.
# Set `APCA_API_KEY_ID` and `APCA_API_SECRET_KEY` in your environment or in a local .env file.
API_KEY = os.getenv("APCA_API_KEY_ID") or os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY") or os.getenv("ALPACA_SECRET_KEY")

# Optional: override the base URL (defaults to the Alpaca paper endpoint)
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")