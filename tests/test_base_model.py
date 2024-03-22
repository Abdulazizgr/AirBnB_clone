#!/usr/bin/python3
""" Unittest file for base_model module """
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """ This runs all the tests for the basemodel class """

    def setUp(self):
        """ Helps to create a object of BaseModel """
        self.my_model = BaseModel()

    def tearDown(self):
        """ Helps to clean up methods """

    def test_str(self):
        """ Test the string representation """
        res = "[BaseModel] ({}) {}".format(
                self.my_model.id, self.my_model.__dict__)

        self.assertEqual(str(self.my_model), res)

    def test_save(self):
        """ Tests the save method """
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model.save()

        my_model_json = self.my_model.to_dict()
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)

    def test_updated_at(self):
        """ Test whether the updated times are not the same """
        first_update = self.my_model.updated_at
        self.my_model.save()
        second_update = self.my_model.updated_at

        self.assertNotEqual(first_update, second_update)
