""" These class defines a set of functions to used to validate information in the entire application """

import re
from passlib.hash import pbkdf2_sha256 as sha256
from app.api.v2.models import cur

class Tools():
    # def __init__(self):
    #     self.values = (int, float)

    #A method to validate user information
    @staticmethod
    def validate_user_info(username, email, phone_number, password, confirm_password):

        if not re.match("^[a-zA-Z0-9_]*$", username):
            return "Username can only contain alphanumeric characters"
        else:
            if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                return "Invalid Email"
            elif len(username.strip()) < 6:
                return "Username should be atleast six characters long"
            elif len(password) < 6:
                return "Password should be atleast six characters long"
            elif password != confirm_password:
                return "Your Passwords Should match"
            else:
                return True

    #A method to validate product information
    @staticmethod
    def validate_products_info(name, category, buying_price, selling_price):

        values = [int, float]

        if not isinstance(values, buying_price):
            return "Invalid Buying price"
        else:
            if not isinstance(selling_price, values):
                return "Invalid Selling price"
            else:
                return True

    @staticmethod
    def get_all_users():
        cur.execute(" SELECT * FROM users ")
        users = cur.fetchall()
        return users

    # The method checks whether a user with similar email, username or phone no exists in the database
    @staticmethod
    def user_exists(email, phone_number, username):
        tools = Tools()
        all_users = tools.get_all_users()

        for user in all_users:
            if user['email'] == email or user['phone_number'] == phone_number or user['username'] == username:
                return True
        else:
            return False

    #The method is used to hash password passed by the users
    @staticmethod
    def generate_hash(password):
        hashed_pass = sha256.hash(password)
        return hashed_pass

    #The method verifies a hashed password
    @staticmethod
    def verify_hash(password, hash):
        verified = sha256.verify(password, hash)
        return True

    





       
