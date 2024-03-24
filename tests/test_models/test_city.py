""" Unit test for City class """
from models.city import City
import unittest
import os
from datetime import datetime


class TestCity(unittest.TestCase):
    """ City class unit tests """

    def setUp(self):
        """ Creating an object of the class """
        self.my_model = city()

    def tearDown(self):
        """ Method to clean up """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_type(self):
        """ Testing the tye of attribute """
        self.assertInstance(self.my_model.id, str)
        self.assertInstance(self.my_model.name, str)
        self.assertInstance(self.my_model.state_id, str)
        self.assertInstance(self.my_model.created_at, datetime)
        self.assertInstance(self.my_model.updated_at, datetime)
