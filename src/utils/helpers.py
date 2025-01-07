import requests

def fetch_data_from_api(url, headers=None):
    """Fetches data from an API endpoint."""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
