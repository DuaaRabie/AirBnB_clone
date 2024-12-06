#!/usr/bin/python3
""" This Module to test Amenity """
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test Amenity """
    def setUp(self):
        """ setup before the testing, create instance """
        self.m = Amenity()

    def test_name_is_str(self):
        """ testing name """
        self.assertIsInstance(self.m.name, str)


if __name__ == '__main__':
    unittest.main()
