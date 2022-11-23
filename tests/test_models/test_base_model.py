"""Module test case."""
import unittest

from models.base_model import BaseModel
from datetime import date


class TestBaseModel(unittest.TestCase):
    """Test class for base model."""

    def setUp(self):
        """To setup for test case."""
        self.base_model = BaseModel()

    def test_created_at(self):
        """Testing if date time is created on instances."""
        self.assertEqual(self.base_model.created_at, date.today())


if __name__ == '__main__':
    unittest.main()
