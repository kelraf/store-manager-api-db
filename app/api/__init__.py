""" These class defines a set of functions to used to validate information in the entire application """

import re
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

    #A method That Gets all The Users
    @staticmethod
    def all_users():

        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        return users



       
