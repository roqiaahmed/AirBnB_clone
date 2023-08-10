#!/usr/bin/python3
""" testing files """
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
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
        storage.new(obj)
        self.assertEqual(storage.all()[obj_key], obj)

    def test_save(self):
        """ check save """
        obj = BaseModel()
        obj_key = "BaseModel" + '.' + obj.id
        self.assertEqual(storage.all()[obj_key], obj)

    def test_reload(self):
        """ check reload """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        storage.save()

        self.assertTrue(os.path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}

        storage.reload()

        self.assertTrue(obj_key in storage.all().keys())
        self.assertEqual(obj.id, storage.all()[obj_key].id)
