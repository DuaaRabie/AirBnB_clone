#!/usr/bin/python3
""" This Module to test City """
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """ Test City """
    def setUp(self):
        """ setup before the testing, create instance """
        self.m = City()

    def test_city_id_is_str(self):
        """ testing city_id """
        self.assertIsInstance(self.m.city_id, str)

    def test_name_is_str(self):
        """ test name """
        self.assertIsInstance(self.m.name, str)


if __name__ == '__main__':
    unittest.main()
