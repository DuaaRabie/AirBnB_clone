import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
   def setUp(self):
       self.bm = BaseModel()

   def test_id_is_string(self):
       self.assertIsInstance(self.bm.id, str)

   def test_created_at_is_datetime(self):
       self.assertIsInstance(self.bm.created_at, datetime)

   def test_updated_at_is_datetime(self):
       self.assertIsInstance(self.bm.updated_at, datetime)

   def test_save_updates_updated_at(self):
       old_updated_at = self.bm.updated_at
       self.bm.save()
       self.assertNotEqual(old_updated_at, self.bm.updated_at)

   def test_to_dict_returns_dict(self):
       self.assertIsInstance(self.bm.to_dict(), dict)

   def test_to_dict_includes_class_name(self):
       self.assertEqual(self.bm.to_dict()['__class__'], 'BaseModel')

   def test_to_dict_includes_id(self):
       self.assertEqual(self.bm.to_dict()['id'], self.bm.id)

   def test_to_dict_includes_created_at_in_iso_format(self):
       self.assertEqual(self.bm.to_dict()['created_at'], self.bm.created_at.isoformat())

   def test_to_dict_includes_updated_at_in_iso_format(self):
       self.assertEqual(self.bm.to_dict()['updated_at'], self.bm.updated_at.isoformat())

if __name__ == '__main__':
   unittest.main()
