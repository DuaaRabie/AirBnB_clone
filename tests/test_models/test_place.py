#!/usr/bin/python3
""" This Module to test Place """
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test Place """
    def setUp(self):
        """ setup before the testing, create instance """
        self.m = Place()

    def test_city_id_is_str(self):
        """ testing city_id """
        self.assertIsInstance(self.m.city_id, str)

    def test_user_id_is_str(self):
        """ test user_id """
        self.assertIsInstance(self.m.user_id, str)

    def test_name_is_str(self):
        """ test name """
        self.assertIsInstance(self.m.name, str)

    def test_description_is_str(self):
        """ test description """
        self.assertIsInstance(self.m.description, str)

    def test_number_rooms_is_int(self):
        """ test number_rooms"""
        self.assertIsInstance(self.m.number_rooms, int)

    def test_number_bathrooms_is_int(self):
        """ test number_bathrooms"""
        self.assertIsInstance(self.m.number_bathrooms, int)

    def test_max_guest_is_int(self):
        """ test max_guest"""
        self.assertIsInstance(self.m.max_guest, int)

    def test_price_by_night_is_int(self):
        """ test price_by_night"""
        self.assertIsInstance(self.m.price_by_night, int)

    def test_latitude_is_float(self):
        """ test latitude"""
        self.assertIsInstance(self.m.latitude, float)

    def test_number_longitude_is_float(self):
        """ test longitude"""
        self.assertIsInstance(self.m.longitude, float)

    def test_number_amenity_ids_list(self):
        """ test amenity_ids"""
        self.assertIsInstance(self.m.amenity_ids, list)   
 

if __name__ == '__main__':
    unittest.main()
