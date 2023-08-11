#!/usr/bin/python3
""" testing files """
import unittest
from models.place import Place

class test_place(unittest.TestCase):
    """ Class test for User """

    def test_attributes(self):
        """None attribute."""
        obj = Place()
        obj.city_id = "50"
        obj.user_id = "321"
        obj.name = "Betty"
        obj.description = "test_description"
        obj.number_rooms = 5
        obj.number_bathrooms = 5
        obj.max_guest = 5
        obj.price_by_night = 5
        obj.latitude = 5.5
        obj.longitude = 5.5
        obj.amenity_ids = ["15", "30", "44"]

        self.assertEqual(obj.city_id, "50")
        self.assertEqual(obj.user_id, '321')
        self.assertEqual(obj.name, 'Betty')
        self.assertEqual(obj.description, 'test_description')
        self.assertEqual(obj.number_rooms, 5)
        self.assertEqual(obj.number_bathrooms, 5)
        self.assertEqual(obj.max_guest, 5)
        self.assertEqual(obj.price_by_night, 5)
        self.assertEqual(obj.latitude, 5.5)
        self.assertEqual(obj.longitude, 5.5)
        self.assertEqual(obj.amenity_ids, ["15", "30", "44"])
