from app.api import Tools 
import uuid

tools = Tools()
all_users = tools.all_users()
validate_data = tools.validate_user_info()


class UserDetails():

    def register(self, username, email, phone_number, password, confirm_password):
        user_info = {}

        #Check If there are users in the database
        if len(all_users) > 0:
            validate = validate_data(username, email, phone_number, password, confirm_password)

            if validate == True:
                for user in all_users:
                    if user['email'] == email:
                        return "User already exists"
                    elif user['username'] == username:
                        return "Username already exits"
                    elif user['phone_number'] == phone_number:
                        return "Phone number already exits"
                else:
                    user_info['username'] = username
                    user_info['email'] = email
                    user_info['phone_number'] = phone_number
                    user_info['password'] = password
                    user_info['confirm_password'] = confirm_password
                    user_info['id'] = uuid.uuid1()
                    user_info['admin'] = False

                    store_user = """ INSERT INTO users; (username, email, phone_number, password, confirm_password) """
