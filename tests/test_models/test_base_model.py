"""Module test case."""
import unittest

from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test class for base model."""

    def setUp(self):
        """To setup for test case."""
        self.base_model = BaseModel()
        model_json = self.base_model.to_dict()
        self.base2 = BaseModel(**model_json)

    def test_created_at(self):
        """Testing if date time is created on instances."""
        self.assertNotEqual(self.base_model.created_at, None)

    def test_uuid_creation(self):
        """Testing id creation on instances."""
        self.assertNotEqual(self.base_model.id, '')

    def test_object_similarity(self):
        """Testing if objects are different."""
        self.assertEqual(False, (self.base_model is self.base2))


if __name__ == '__main__':
    unittest.main()
