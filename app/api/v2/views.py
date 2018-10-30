from flask import jsonify, make_response, request, json, request
from flask_restful import Resource
import datetime
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt

#Local imports
from .models.users import UserDetails as users
from app.api import Tools as tools
from .models.products import ProductsDetails as products
from app.api.v2.models import conn, cur




""" Routes for Users """
class Users(Resource):
    @jwt_required
    def post(self):
        user_info = request.get_json()

        username = user_info['username']
        email = user_info['email']
        phone_number = user_info['phone_number']
        password = user_info['password']
        confirm_password = user_info['confirm_password']

        response = users.register(username, email, phone_number, password, confirm_password)

        if response == True:
            return make_response(jsonify({"Status" : "Ok", "Message" : "User Registered Successfully"}), 201)
        return make_response(jsonify({"Status" : "CONFLICT", "Message" : "User Not Created", "Reason" : response}), 409)

    @jwt_required
    def get(self):
        all_users = users.get_all_users()
        if len(all_users) > 0:
            return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull", "users" : all_users, "No of Users" : len(all_users)}), 200)
        return make_response(jsonify({"Status" : "NOT FOUND", "Message" : "The Database does not have any users"}), 404)

class Get_user_by_id(Resource):

    #Get user by Id
    @jwt_required
    def get(self, id):
        query = """ SELECT * FROM users WHERE id = %s """
        user = cur.execute(query, (id,))
        if user:
            return make_response(jsonify({"Status" : "Ok", "Message" : "Successful", "user" : user}), 200)
        return make_response(jsonify({"Status" : "NOT FOUND", "Message" : "User does not exists"}), 200)

class Login(Resource):
    def post(self):
        user_info = request.get_json()

        username = user_info['username']
        password = user_info['password']
        current_user = users.login(username)
        if current_user:
            verified_pass = tools.verify_hash(password, current_user['password'])
            if verified_pass != True:
                return make_response(jsonify({"Status" : "NOT FOUND", "Message" : "Invalid Password"}), 404)
            
            #Generate access token
            exp = datetime.timedelta(minutes = 60)
            identity = current_user
            access_token = create_access_token(identity, exp)
            refresh_token = create_refresh_token(identity = current_user)

            return make_response(jsonify({"Status" : "Ok", "Message" : "Successfully Logged in as {}".format(username),
            "access_token" : access_token, "refresh_token" : refresh_token}), 200)
        return make_response(jsonify({"Status" : "NOT FOUND", "Message" : current_user}), 404)


""" Routes for Products """

class Products(Resource):
    
    @jwt_required
    def post(self):
        product_info = request.get_json()

        name = product_info['name']
        category = product_info['category']
        buying_price = product_info['buying_price']
        selling_price = product_info['selling_price']
        description = product_info['description']

        response = products.create_product(name, category, buying_price, selling_price, description)
        if response == True:
            return make_response(jsonify({"Status" : "CREATED", "Message" : "Product Created Successfully"}), 201)
        else:
            return make_response(jsonify({"Status" : "CONFLICT", "Message" : "Product Product not created"}), 409)

    @jwt_required
    def get(self):
        response = products.get_all_products()        
        if len(response) > 0:
            return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull", "Products" : response, "No of Products" : len(response)}), 200)
        return make_response(jsonify({"Status" : "NOT FOUND", "Message" : "The Database does not have products"}), 404)

