import random
import string


class User:
    # Class that generates new instances of user

    user_list = []  # empty list

    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def user_save(self):
        # saves user object into user object.

        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        return cls.user_list

        # End of user class

####

class Credentials:

   # Class that generates new instances of credential object.

        credential_list = []

        def __init__(self, account_name, account_username, account_password):
            self.account_name = account_name
            self.account_username = account_username
            self.account_password = account_password

        @classmethod
        def check_user_exist(cls, account_username, password):

            # Method that checks if a user exist from user list.

            for user in User.user_list:
                if user.user_name == account_username and user.password == password:
                    return True
                return False

        def save_account(self):

            # save_account saves credential object into credential object.

            Credentials.credential_list.append(self)

        def delete_account(self):

            # delete_account method removes a saved credential from credential list.

            Credentials.credential_list.remove(self)

        @classmethod
        def display_accounts(cls):

            # Method that returns the credential list.

            return cls.credential_list

        def generate_password(self):
            char = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"

            gen_pass = "".join(random.choice(char) for _ in range(8))

            return gen_pass

        # End of class credentials
