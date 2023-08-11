#!/usr/bin/python3
""" testing files """
import unittest
from models.amenity import Amenity

class test_amenity(unittest.TestCase):
    """ Class test for amenity """

    def test_attributes(self):
        """None attribute."""
        obj = Amenity()
        obj.name = "Bar"
        self.assertEqual(obj.name, 'Bar')
