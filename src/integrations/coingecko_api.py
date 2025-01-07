import requests

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

def get_coin_gecko_data(symbol):
    """Fetches market data from CoinGecko."""
    url = f"{COINGECKO_API_URL}/simple/price?ids={symbol}&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinGecko: {e}")
        return None
