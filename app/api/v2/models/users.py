from app.api import Tools 
import uuid
from app.api.v2.models import conn, cur, cur2

tools = Tools()
# all_users = tools.all_users()



class UserDetails():

    @staticmethod
    def register(username, email, phone_number, password, confirm_password):

        user = tools.user_exists(email, phone_number, username)
        if user == False:
            hash_pass = tools.generate_hash(password)
            if hash_pass:
                #If The user does not exist validate the information provided and store the user in the database
                validate = tools.validate_user_info(username, email, phone_number, password, confirm_password)

                if validate == True:
                    query = """ INSERT INTO users(username, email, phone_number, password, confirm_password) VALUES(%s, %s, %s, %s, %s)"""

                    cur.execute(query, (username, email, phone_number, hash_pass, confirm_password))
                    conn.commit()
                    return True
                return validate

            return "The Password could not be hashed"

        #If user does exist 
        return "User already Exists"

    # The login method
    @staticmethod
    def login(username):
        query = """ SELECT * FROM users WHERE username = %s """
        cur.execute(query, (username,))
        user = cur.fetchone()
        if user:
            return user
        return "User {}, does not exist".format(username)

    @staticmethod
    def get_all_users():
        cur.execute(" SELECT * FROM users ")
        users = cur.fetchall()
        return users
