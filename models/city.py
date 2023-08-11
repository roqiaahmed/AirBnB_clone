#!/usr/bin/python3
""" Class BaseModel """
from models.base_model import BaseModel

class City(BaseModel):
    """
    User class
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)