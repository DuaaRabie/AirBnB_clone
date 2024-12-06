#!/usr/bin/python3
""" This module is Testing Amenity """
import unittest
from models.amenity import Amenity
from datetime import datetime


def test_amenity_creation(self):
        """Test the creation of an Amenity object."""
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")
        self.assertTrue(isinstance(amenity.id, str))
        self.assertTrue(isinstance(amenity.created_at, datetime))
        self.assertTrue(isinstance(amenity.updated_at, datetime))

    def test_default_amenity_name(self):
        """Test the default value of the name attribute in Amenity."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
