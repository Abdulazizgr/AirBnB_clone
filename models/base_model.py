#!/usr/bin/python3
""" This is the base model class that defines all the attributes
    and methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """ The base class for which all all classes will inherit from """

    def __init__(self, *args, **kwargs):
        """ Class Constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def __str__(self):
        """ Method to print the string """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """ Updates the attributes - updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary for all the keys/values of the dict """
        dict_copy = self.__dict__.copy()

        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        return dict_copy
