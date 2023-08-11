#!/usr/bin/python3
""" testing files """
import unittest
from models.state import State

class test_state(unittest.TestCase):
    """ Class test for User """

    def test_attributes(self):
        """None attribute."""
        obj = State()
        obj.name = "Bar"
        self.assertEqual(obj.name, 'Bar')
