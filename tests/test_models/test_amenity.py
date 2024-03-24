""" Unit test for Amenity class """
from models.amenity import Amenity
import unittest
import os
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Amenity class unit tests """

    def setUp(self):
        """ Creating an object of the class """
        self.my_model = Amenity()

    def tearDown(self):
        """ Method to clean up """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_type(self):
        """ Testing the tye of attribute """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.name, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
