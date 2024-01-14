#!/usr/bin/python3
""" This Module to test file storage """
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test FileStorage """
    def setUp(self):
        """ setup before testing """
        self.s = FileStorage()
        self.m = BaseModel()
        self.s.new(self.m)

    def test_all(self):
        """ tests all returns dictionary """
        self.assertIsInstance(self.s.all(), dict)
        
    def test_new(self):
        """ Tests new sets object """
        self.assertIn("BaseModel.{}".format(self.m.id), self.s.all())

    def test_save(self):
        """ tests save writes to file """
        self.s.save()
        self.assertTrue(os.path.isfile("/root/AirBnB_clone/file.json"))

    def test_reload(self):
        """ test_reload_reads_from_file """
        self.s.save()
        s2 = FileStorage()
        s2.reload()
        self.assertIn("BaseModel.{}".format(self.m.id), s2.all())

if __name__ == '__main__':
    unittest.main()
