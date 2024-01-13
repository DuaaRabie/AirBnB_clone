import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
 def setUp(self):
     self.fs = FileStorage()
     self.bm = BaseModel()
     self.fs.new(self.bm)

 def test_all_returns_dict(self):
     self.assertIsInstance(self.fs.all(), dict)

 def test_new_sets_object(self):
     self.assertIn("BaseModel.{}".format(self.bm.id), self.fs.all())

 def test_save_writes_to_file(self):
     self.fs.save()
     self.assertTrue(os.path.exists(FileStorage.__file_path))

 def test_reload_reads_from_file(self):
     self.fs.save()
     fs2 = FileStorage()
     fs2.reload()
     self.assertIn("BaseModel.{}".format(self.bm.id), fs2.all())

if __name__ == '__main__':
 unittest.main()
