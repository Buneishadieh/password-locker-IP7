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

def display_users():
    # Function to diplay users.
    return User.display_users()

def login_user(user_name, password):
    # function that checks whether a user exists and then logs the user in.

    check_user_exist = Credentials.check_user_exist(user_name, password)
    return check_user_exist

####

def create_credential(account_name, account_username, account_password):
    # Function to create a new credential.

    new_credential = Credentials(account_name, account_username, account_password)
    return new_credential


def save_credential(credential):
    # Function to save new account credentials.

    credential.save_account()


def delete_account(credential):
    # Function to delete a credential.

    credential.delete_account()


def display_accounts():
    # Function that returns all the saved credential.

    return Credentials.display_accounts()


def generate_password():
    # Function that generates random password.

    password_gen = Credentials.generate_password()
    return password_gen

def main():
  print("welcome to password locker...")
  print('\n')
  while True:
      print('.' * 10)
      short_code = input(
          "Use the following short codes: CA- create a new user account, LOG - login into your account, ESC - exit from password locker \n").lower().strip()
      print('.' * 10)

      if short_code == "esc":
          print("Goodbye!")
          break

      elif short_code == "ca":
          print("Sign Up")
          print('-' * 10)
          user_name = input("User_name: ")
          password = input("Password: ")
          email = input("Email: ")

          save_user(create_user(user_name, password, email))
          print('\n')

          print("account has been created succesfully!")
          print('\n')
          print('-' * 10)

