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
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
    
    def __str__(self):
        """ Method to print the string """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)
