import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a class to ensure the file path is cleaned before each test"""
        cls.file_path = "file.json"
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)
        cls.storage = FileStorage()
        cls.storage.reload()  # Reload any objects from file (if exists)

    def test_save_updates_updated_at(self):
        """Test if save() updates the updated_at attribute"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        new_updated_at = my_model.updated_at

        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(isinstance(new_updated_at, datetime))

    def test_save_persist_to_file(self):
        """Test if save() properly saves the object to the file"""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        my_model.save()

        # Reload objects from the storage and check if the object is in the dictionary
        self.storage.reload()
        all_objs = self.storage.all()

        # Check if the object is stored correctly in the dictionary
        self.assertIn(f"BaseModel.{my_model.id}", all_objs)
        stored_model = all_objs[f"BaseModel.{my_model.id}"]
        self.assertEqual(stored_model.name, "Test Model")
        self.assertEqual(stored_model.my_number, 42)

    def test_save_creates_file(self):
        """Test if the file is created after calling save()"""
        my_model = BaseModel()
        my_model.save()

        self.assertTrue(os.path.exists(self.file_path))

    def test_save_overwrites_file(self):
        """Test if multiple saves overwrite the file with the latest objects"""
        my_model_1 = BaseModel()
        my_model_1.name = "Model 1"
        my_model_1.save()

        my_model_2 = BaseModel()
        my_model_2.name = "Model 2"
        my_model_2.save()

        # Reload objects and check that only the second model is in the file
        self.storage.reload()
        all_objs = self.storage.all()

        self.assertIn(f"BaseModel.{my_model_2.id}", all_objs)
        self.assertNotIn(f"BaseModel.{my_model_1.id}", all_objs)

    @classmethod
    def tearDownClass(cls):
        """Clean up the created file after tests"""
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)

if __name__ == "__main__":
    unittest.main()
