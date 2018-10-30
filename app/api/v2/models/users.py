from app.api import Tools 
import uuid
from app.api.v2.models import conn, cur

tools = Tools()
# all_users = tools.all_users()



class UserDetails():

    @staticmethod
    def register(username, email, phone_number, password, confirm_password):

        user = tools.user_exists(email, phone_number, username)
        if user == False:

            #If The user does not exist validate the information provided and store the user in the database
            validate = tools.validate_user_info(username, email, phone_number, password, confirm_password)

            if validate == True:
                query = """ INSERT INTO users(username, email, phone_number, password, confirm_password) VALUES(%s, %s, %s, %s, %s)"""

                cur.execute(query, (username, email, phone_number, password, confirm_password))
                conn.commit()
                return True
            return validate

        #If user does exist 
        return "User already Exists"

    #The login method
    @staticmethod
    def login(username, password):
        users_class = UserDetails()
        users = users_class.get_all_users()

        for user in users:
            if user['username'] == username and user['password'] == password:
                return True
        else:
            return "The user does not exist"

    @staticmethod
    def get_all_users():
        cur.execute(" SELECT * FROM users ")
        users = cur.fetchall()
        return users