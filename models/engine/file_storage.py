#!/usr/bin/python3
""" class FileStorage
    serializes instances to a JSON file
    and deserializes JSON file to instances """
import json
import uuid
import os
from datetime import datetime
# from models.user import User
# from models.base_model import BaseModel

class FileStorage:
    """ Construct """

    __file_path = ("file.json")
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return self.__objects

    def new(self, obj):
        """ sets in dictionary the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes objectss to the JSON file (path: __file_path) """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """ Reload the file """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fname:
                l_json = json.load(fname)
                for key, val in l_json.items():
                    if '__class__' in val:
                        obj_class = eval(val['__class__'])
                        obj = obj_class(**val)
                        FileStorage.__objects[key] = obj
