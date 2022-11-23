import unittest
from models.base_model import BaseModel
from datetime import date

"""unit test module for base model class"""

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_created_at(self):
        self.assertEqual(self.base_model.created_at, date.today())

if __name__ == '__main__':
    unittest.main()
