import unittest
from src.database import get_connection, initialize_database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        initialize_database()

    def test_connection(self):
        conn = get_connection()
        self.assertIsNotNone(conn)

    def test_trade_table_exists(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='trades'")
        self.assertIsNotNone(cursor.fetchone())
