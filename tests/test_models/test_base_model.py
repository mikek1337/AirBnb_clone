"""Module test case."""
import unittest

from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test class for base model."""

    def setUp(self):
        """To setup for test case."""
        self.base_model = BaseModel()

    def test_created_at(self):
        """Testing if date time is created on instances."""
        self.assertNotEqual(self.base_model.created_at, None)

    def test_uuid_creation(self):
        self.assertNotEqual(self.base_model.id, '');

    def test_save_fun(self):
        """Testing if save function updates updated_at in __dict__."""
        self.base_model.save()
        self.assertEqual(self.base_model.__dict__['updated_at'], datetime.now())


if __name__ == '__main__':
    unittest.main()
