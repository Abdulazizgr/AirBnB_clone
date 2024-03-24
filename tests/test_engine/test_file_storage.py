""" Unit test for file storage """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """ FileStorage class unit tests """

    def setUp(self):
        """ Creating an object of the class """
        self.my_storage = FileStorage()

    def tearDown(self):
        """ Method to clean up """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_type(self):
        """ Check and assert the attribute type """

        self.assertEqual(type(self.my_storage.all()), dict)
