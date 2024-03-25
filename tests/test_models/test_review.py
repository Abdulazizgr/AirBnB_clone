#!/usr/bin/python3
""" Unit test for Review class """
from models.review import Review
import unittest
import os
from datetime import datetime


class TestReview(unittest.TestCase):
    """ Review class unit tests """

    def setUp(self):
        """ Creating an object of the class """
        self.my_model = Review()

    def tearDown(self):
        """ Method to clean up """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_type(self):
        """ Testing the tye of attribute """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.place_id, str)
        self.assertIsInstance(self.my_model.user_id, str)
        self.assertIsInstance(self.my_model.text, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
