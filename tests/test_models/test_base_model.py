#!/usr/bin/python3
""" testing files """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class test_for_base_model(unittest.TestCase):
    """ Class test for BaseModel """

    def setUp(self):
        """ Create instance """
        self.base_model = BaseModel()

    def tearDown(self):
        """ delete json file """
        del self.base_model

    def test_attributes(self):
        """None attribute."""
        object_test = BaseModel(None)
        self.assertTrue(hasattr(object_test, 'id'))
        self.assertTrue(hasattr(object_test, 'created_at'))
        self.assertTrue(hasattr(object_test, 'updated_at'))

    def test_to_dict(self):
        """ check dict """
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['__name__'], 'BaseModel')
        self.assertEqual(type(base_model_dict['created_at']), str)
        self.assertEqual(type(base_model_dict['updated_at']), str)

    def test_str_representation(self):
        base_model_str = str(self.base_model)
        self.assertEqual(base_model_str, "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__))

if __name__ == '__main__':
    unittest.main()
