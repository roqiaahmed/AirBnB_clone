#!/usr/bin/python3
""" testing files """
import unittest
from models.user import User

class test_user(unittest.TestCase):
    """ Class test for User """

    def test_attributes(self):
        """None attribute."""
        obj = User()
        obj.email = "airbnb@mail.com"
        obj.password = "root"
        obj.first_name = "Betty"
        obj.last_name = "Bar"
        self.assertEqual(obj.email, "airbnb@mail.com")
        self.assertEqual(obj.password, 'root')
        self.assertEqual(obj.first_name, 'Betty')
        self.assertEqual(obj.last_name, 'Bar')
