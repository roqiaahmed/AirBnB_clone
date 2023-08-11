#!/usr/bin/python3
""" testing files """
import unittest
from models.review import Review

class test_review(unittest.TestCase):
    """ Class test for review """

    def test_attributes(self):
        """None attribute."""
        obj = Review()
        obj.place_id = "30"
        obj.user_id = "50"
        obj.text = "Betty"

        self.assertEqual(obj.place_id, '30')
        self.assertEqual(obj.user_id, '50')
        self.assertEqual(obj.text, 'Betty')
