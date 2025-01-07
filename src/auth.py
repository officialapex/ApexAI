from flask import request, abort

API_KEYS = ["your-api-key-here"]

def authenticate():
    """Validates the API key in the request header."""
    api_key = request.headers.get("Authorization")
    if not api_key or api_key.split("Bearer ")[-1] not in API_KEYS:
        abort(401, "Unauthorized: Invalid API Key")
