#!/usr/bin/python3
""" testing files """
import unittest
from models.city import City

class test_city(unittest.TestCase):
    """ Class test for User """

    def test_attributes(self):
        """None attribute."""
        obj = City()
        obj.state_id = "15"
        obj.name = "Betty"
        self.assertEqual(obj.state_id, "15")
        self.assertEqual(obj.name, 'Betty')
