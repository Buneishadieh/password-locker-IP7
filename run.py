#!/Desktop/password_locker/env python3.7
from password_locker import User
from password_locker import Credentials


def create_user(user_name, password, email):
    # Function to create a new user.

    new_user = User(user_name, password, email)
    return new_user


def save_user(user):
    # Function to save user.

    user.user_save()