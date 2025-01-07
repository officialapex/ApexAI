from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Apex AI!"

@app.route("/markets", methods=["GET"])
def get_markets():
    # Example response for market data
    market_data = {
        "BTC/USD": {"price": 45000, "change": 1.2},
        "ETH/USD": {"price": 3000, "change": -0.5},
    }
    return jsonify(market_data)

@app.route("/trade", methods=["POST"])
def execute_trade():
    # Simulate a successful trade
    response = {
        "status": "success",
        "order_id": "12345"
    }
    return jsonify(response), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
