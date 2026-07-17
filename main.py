from alpaca.trading.client import TradingClient
from config import API_KEY, SECRET_KEY, ALPACA_BASE_URL

if not API_KEY or not SECRET_KEY:
    print("API_KEY or SECRET_KEY not set. Copy .env.example to .env and fill values.")
    print("Install dependencies: pip install alpaca-py python-dotenv")
    raise SystemExit(1)

# Print masked debug info (does not reveal secrets)
masked_key = API_KEY[:4] + "..." + API_KEY[-4:] if API_KEY and len(API_KEY) > 8 else "(hidden)"
print(f"Using API key: {masked_key}")
print(f"Using base URL: {ALPACA_BASE_URL}")

client = TradingClient(
    api_key=API_KEY,
    secret_key=SECRET_KEY,
    paper=True
)

try:
    account = client.get_account()
except Exception as e:
    print("Failed to retrieve account:", e)
    raise

print("Connected!")
print(f"Status        : {account.status}")
print(f"Cash          : ${account.cash}")
print(f"Buying Power  : ${account.buying_power}")