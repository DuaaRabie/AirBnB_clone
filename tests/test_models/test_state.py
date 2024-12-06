#!/usr/bin/python3
""" This Module to test State"""
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """ Test State """
    def setUp(self):
        """ setup before the testing, create instance """
        self.m = State()

    def test_name_is_str(self):
        """ test the name """
        self.assertIsInstance(self.m.name, str)


if __name__ == '__main__':
    unittest.main()
