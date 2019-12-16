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

    def test_user_save(self):
        # Test case to test if the user object is saved into the user_list.

        self.new_user.user_save()

        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        # Test to check whether we can save multiple user objects.

        self.new_user.user_save()
        test_user = User("Rick", "2344", "rick@gmail.com")
        test_user.user_save()
        self.assertEqual(len(User.user_list), 2)

    def test_display_users(self):
        self.assertEqual(User.display_users(), User.user_list)