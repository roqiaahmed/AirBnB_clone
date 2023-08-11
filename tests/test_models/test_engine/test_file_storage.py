#!/usr/bin/python3
""" testing files """
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class test_storage(unittest.TestCase):
    """ Class test for  FileStorage"""

    def setUp(self):
        """ check empty """
        try:
            os.remove('file.json')
        except Exception:
            pass
        storage._FileStorage__objects = {}

    def tearDown(self):
        """ check remove class """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_no_obj(self):
        """ check empty class  """
        self.assertEqual(storage.all(), {})

    def test_storge_all(self):
        """ check  all function """
        obj = storage.all()
        self.assertEqual(type(obj), dict)
        self.assertIsNotNone(obj)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """ check new method """
        obj = BaseModel(id='321')
        obj_key = "BaseModel" + '.' + obj.id

        obj1 = User(id='1')
        obj1_key = 'User' + '.' + obj1.id

        obj2 = State()
        obj2_key = 'State' + '.' + obj2.id

        obj3 = City()
        obj3_key = 'City' + '.' + obj3.id

        obj4 = Amenity()
        obj4_key = 'Amenity' + '.' + obj4.id

        obj5 = Place()
        obj5_key = 'Place' + '.' + obj5.id

        obj6 = Review()
        obj6_key = 'Review' + '.' + obj6.id

        storage.new(obj)
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)

        self.assertEqual(storage.all()[obj_key], obj)
        self.assertEqual(storage.all()[obj1_key], obj1)
        self.assertEqual(storage.all()[obj2_key], obj2)
        self.assertEqual(storage.all()[obj3_key], obj3)
        self.assertEqual(storage.all()[obj4_key], obj4)
        self.assertEqual(storage.all()[obj5_key], obj5)
        self.assertEqual(storage.all()[obj6_key], obj6)

    def test_save(self):
        """ check save """
        obj = BaseModel()
        obj_key = "BaseModel" + '.' + obj.id

        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id

        obj2 = State()
        obj2_key = 'State' + '.' + obj2.id

        obj3 = City()
        obj3_key = 'City' + '.' + obj3.id

        obj4 = Amenity()
        obj4_key = 'Amenity' + '.' + obj4.id

        obj5 = Place()
        obj5_key = 'Place' + '.' + obj5.id

        obj6 = Review()
        obj6_key = 'Review' + '.' + obj6.id

        self.assertEqual(storage.all()[obj_key], obj)
        self.assertEqual(storage.all()[obj1_key], obj1)
        self.assertEqual(storage.all()[obj2_key], obj2)
        self.assertEqual(storage.all()[obj3_key], obj3)
        self.assertEqual(storage.all()[obj4_key], obj4)
        self.assertEqual(storage.all()[obj5_key], obj5)
        self.assertEqual(storage.all()[obj6_key], obj6)

    def test_reload(self):
        """ check reload """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id

        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id

        obj2 = State()
        obj2_key = 'State' + '.' + obj2.id

        obj3 = City()
        obj3_key = 'City' + '.' + obj3.id

        obj4 = Amenity()
        obj4_key = 'Amenity' + '.' + obj4.id

        obj5 = Place()
        obj5_key = 'Place' + '.' + obj5.id

        obj6 = Review()
        obj6_key = 'Review' + '.' + obj6.id

        storage.save()

        self.assertTrue(os.path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}

        storage.reload()

        self.assertTrue(obj_key in storage.all().keys())
        self.assertEqual(obj.id, storage.all()[obj_key].id)

        self.assertTrue(obj1_key in storage.all().keys())
        self.assertEqual(obj1.id, storage.all()[obj1_key].id)

        self.assertTrue(obj2_key in storage.all().keys())
        self.assertEqual(obj2.id, storage.all()[obj2_key].id)

        self.assertTrue(obj3_key in storage.all().keys())
        self.assertEqual(obj3.id, storage.all()[obj3_key].id)

        self.assertTrue(obj4_key in storage.all().keys())
        self.assertEqual(obj4.id, storage.all()[obj4_key].id)

        self.assertTrue(obj5_key in storage.all().keys())
        self.assertEqual(obj5.id, storage.all()[obj5_key].id)

        self.assertTrue(obj6_key in storage.all().keys())
        self.assertEqual(obj6.id, storage.all()[obj6_key].id)
