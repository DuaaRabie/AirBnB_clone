#!/usr/bin/python3
""" This Module to test BaseModel """
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test BaseModel """
    def setUp(self):
        """ setup before the testing, create instance """
        self.m = BaseModel()

    def test_id_is_str(self):
        """ testing id """
        self.assertIsInstance(self.m.id, str)

    def test_created_at_is_datetime(self):
        """ test created at """
        self.assertIsInstance(self.m.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """ test updated at """
        self.assertIsInstance(self.m.updated_at, datetime)

    def test_updating_updated_at(self):
        """ test updating updated at """
        old_updated_at = self.m.updated_at
        self.m.save()
        self.assertNotEqual(old_updated_at, self.m.updated_at)

    def test_to_dict_returns_dict(self):
        """ test to dict returns dictionary """
        self.assertIsInstance(self.m.to_dict(), dict)

    def test_to_dict_includes_class_id(self):
        """ test to dict include class name and id """
        self.assertEqual(self.m.to_dict()['__class__'], 'BaseModel')
        self.assertEqual(self.m.to_dict()['id'], self.m.id)

    def test_to_dict_created_updated_iso_format(self):
        """ test to dict include created at/updated at in iso """
        cf = self.m.created_at.isoformat()
        uf = self.m.updated_at.isoformat()
        self.assertEqual(self.m.to_dict()['created_at'], cf)
        self.assertEqual(self.m.to_dict()['updated_at'], uf)


if __name__ == '__main__':
    unittest.main()
