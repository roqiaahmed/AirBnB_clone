#!/usr/bin/python3
""" Class BaseModel """
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ Construct """

    def __init__(self, *args, **kwargs):
        """initialization"""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            'storage.new(self)''dont forget to add it when u finish the file of storage <<<<<<<<<<<<<<<<<'

    def save(self):
        """ save function """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return a dictonary """
        data = self.__dict__.copy()
        data['__name__'] =  self.__class__.__name__
        data['created_at'] =  self.created_at.isoformat()
        data['updated_at'] =  self.updated_at.isoformat()
        return data

    def __str__(self):
        """ String """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
