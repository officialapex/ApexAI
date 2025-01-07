from transformers import pipeline

def analyze_market_sentiment(market_data):
    """Analyze sentiment of market data using an AI model."""
    sentiment_model = pipeline("sentiment-analysis")
    sentiments = {}

    for symbol, data in market_data.items():
        analysis = sentiment_model(f"The price of {symbol} is {data['price']}.")
        sentiments[symbol] = analysis[0]["label"]

    return sentiments
