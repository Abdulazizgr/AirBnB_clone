#!/usr/bin//python3
"""
    FileStorage module that helps to maintain persistency
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
        It serializes instances to a JSON file and
        deserializes JSON file to instances
    """

    """ Private class attributes """

    __file_path = "file.json"
    __objects = {}

    """ Public instance methods """

    def all(self):
        """ It returns all the dictionary objects """

        return FileStorage.__objects

    def new(self, obj):
        """
        It sets the object with corresponding key
        which is class_name.id

        Args:
            obj: the object saved int __objects dictionary

        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialization of dictionary to json file """

        data = FileStorage.__objects
        file_path = FileStorage.__file_path
        data_dict = {key: data[key].to_dict() for key in data.keys()}

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data_dict, file)

    def reload(self):
        """ Deserialization of json file to a python object """

        try:
            file_path = FileStorage.__file_path
            with open(file_path, "r", encoding="UTF-8") as file:
                data = json.load(file)

                for d in data.values():
                    if d["__class__"]:
                        class_name = d["__class__"]
                        del d["__class__"]
                    self.new(eval(class_name)(**d))
        except FileNotFoundError:
            pass
