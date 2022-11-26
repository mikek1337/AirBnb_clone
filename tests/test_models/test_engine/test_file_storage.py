"""Test module for the storage engine."""

import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test class."""

    def setUp(self):
        """Setup instance."""
        self.base_model = BaseModel()
        self.base_model.name = "Mikias"
        self.base_model.number = 989

    def test_storage_save(self):
        """Test if object is saved to a file."""
        storage.new(self.base_model.to_dict())
        storage.save()


if __name__ == "__main__":
    unittest.main()
