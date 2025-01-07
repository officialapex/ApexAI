import requests

BINANCE_API_URL = "https://api.binance.com/api/v3"

def get_binance_ticker(symbol):
    """Fetches ticker price data for a given symbol from Binance."""
    url = f"{BINANCE_API_URL}/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Binance ticker: {e}")
        return None
