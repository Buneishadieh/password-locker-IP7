import unittest

from password_locker import User
from password_locker import Credentials


class TestUser(unittest.TestCase):

    # Test that defines test cases for the user class behaviours

    def setUp(self):
        # set up method to run before each test cases

        self.new_user = User("Mike", "8299", "theemike@gmail.com")

    def test_init(self):
        # Test case to test if the object is initialized properly

        self.assertEqual(self.new_user.user_name, "Mike")
        self.assertEqual(self.new_user.password, "8299")
        self.assertEqual(self.new_user.email, "theemike@gmail.com")

    def tearDown(self):
        # Method that cleans up after each case has run.

        User.user_list = []

    