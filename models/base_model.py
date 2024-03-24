#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage 


class BaseModel:
    """
    Base class for models with common attributes and methods.

    Attributes:
        id (str): Unique identifier for the model.
        created_at (datetime): Timestamp indicating the creation
        time.
        updated_at (datetime): Timestamp indicating the last update
        time.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.fromisoformat(value)
                elif key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel.
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """
        Updates the 'updated_at' attribute with the current timestamp.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns:
            dict: Dictionary representation of the BaseModel instance.
        """
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict
