import requests

TRADINGVIEW_BASE_URL = "https://api.tradingview.com"

def get_tradingview_data(symbol):
    """Fetches market data from TradingView."""
    url = f"{TRADINGVIEW_BASE_URL}/data/{symbol}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from TradingView: {e}")
        return None
