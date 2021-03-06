from app.api import Tools 
import uuid
from werkzeug.security import generate_password_hash
from ..models import conn, cur

tools = Tools()


class UserDetails():

    @staticmethod
    def register(username, email, phone_number, password, confirm_password):

        user = tools.user_exists(email, phone_number, username)
        if not user:
            hash_pass_1 = generate_password_hash(password)
            hash_pass_2 = generate_password_hash(confirm_password)

            if hash_pass_1 and hash_pass_2:

                #If The user does not exist validate the information provided and store the user in the database
                validate = tools.validate_user_info(username, email, phone_number, password, confirm_password)

                if validate == True:
                    user_infor = {}
                    user_infor['admin'] = False
                    query = """ INSERT INTO users(username, email, phone_number, admin, password, confirm_password) VALUES(%s, %s, %s, %s, %s, %s)"""

                    cur.execute(query, (username, email, phone_number, user_infor['admin'], hash_pass_1, hash_pass_2))
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

    @staticmethod
    def get_user_id(id):
        query = """ SELECT * FROM users WHERE id = %s """
        cur.execute(query, (id,))
        user = cur.fetchone()
        return user

    @staticmethod
    def delete_user(username):
        query = """ SELECT * FROM users """
        cur.execute(query)
        users = cur.fetchall()
        if not users:
            return "There no users in the database"
        for user in users:
            if user['username'] == username:
                query = """ DELETE FROM users WHERE username = %s """
                cur.execute(query, (username,))
                conn.commit()
                return True
        return "user does not exist"

    @staticmethod
    def get_user_by_email(username):
        query = """ SELECT * FROM users  """
        cur.execute(query)
        users = cur.fetchall()
        if users:
            for user in users:
                if user['username'] == username:
                    return user
        return "The user does not exist"

    @staticmethod
    def update_user_infor(username, email, phone_number, password, confirm_password):
        query = """ SELECT * FROM users """
        cur.execute(query)
        users = cur.fetchall()

        if users:
            for user in users:
                if user['username'] == username:
                    validate = tools.validate_user_info(username, email, phone_number, password, confirm_password)
                    if validate == True:
                        hash_pass_1 = generate_password_hash(password)
                        hash_pass_2 = generate_password_hash(confirm_password)
                        query = """ UPDATE users SET email = %s, phone_number = %s, password = %s, confirm_password = %s
                         WHERE username = %s """
                        cur.execute(query, (email, phone_number, hash_pass_1, hash_pass_2, username))
                        conn.commit()
                        return True
                    return validate
            return "The user does not exist"
        return "There are no users in the database"