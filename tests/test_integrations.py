import unittest
from src.integrations.binance_api import get_binance_ticker

class TestBinanceAPI(unittest.TestCase):
    def test_get_binance_ticker(self):
        symbol = "BTCUSDT"
        response = get_binance_ticker(symbol)
        self.assertIsNotNone(response)
        self.assertIn("price", response)
