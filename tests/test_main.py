import unittest
from src.main import app

class TestMainApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Welcome to Apex AI!")

    def test_markets(self):
        response = self.client.get("/markets")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("BTC/USD", data)
