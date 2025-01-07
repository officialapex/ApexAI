import unittest
from src.logger import get_logger

class TestLogger(unittest.TestCase):
    def test_logger(self):
        logger = get_logger("test_logger")
        self.assertIsNotNone(logger)
        self.assertEqual(logger.name, "test_logger")
