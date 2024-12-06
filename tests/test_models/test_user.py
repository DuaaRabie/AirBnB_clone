#!/usr/bin/python3
""" This Module to test BaseModel """
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """ Test BaseModel """
    def setUp(self):
        """ setup before the testing, create instance """
        self.m = User()

    def test_emsil_is_str(self):
        """ testing id """
        self.assertIsInstance(self.m.email, str)

    def test_password_is_str(self):
        """ test password """
        self.assertIsInstance(self.m.password, str)

    def test_first_name_is_str(self):
        """ test first name """
        self.assertIsInstance(self.m.first_name, str)

    def test_last_name_is_str(self):
        """ test last name """
        self.assertIsInstance(self.m.last_name, str)


if __name__ == '__main__':
    unittest.main()
