""" Unittest for the User class file """
from models.user import User
import unittest
import os
from datetime import datetime


class TestUser(unittest.TestCase):
    """ User class unit tests """

    def setUp(self):
        """ Creating an object of the class """
        self.my_model = User()

    def tearDown(self):
        """ Method to clean up """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_type(self):
        """ Check and assert the instance type """
        self.assertInstance(self.my_model.id, str)
        self.assertInstance(self.my_model.email, str)
        self.assertInstance(self.my_model.password, str)
        self.assertInstance(self.my_model.first_name, str)
        self.assertInstance(self.my_model.last_name, str)
        self.assertInstance(self.my_model.created_at, datetime)
        self.assertInstance(self.my_model.updated_at, datetime)
