from flask import jsonify, make_response, request, json, request
from flask_restful import Resource
from .models.users import UserDetails as users
from .models.products import ProductsDetails as products
from app.api.v2.models import conn, cur




""" Routes for Users """
class Users(Resource):
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

    def get(self):
        all_users = users.get_all_users()
        if len(all_users) > 0:
            return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull", "users" : all_users, "No of Users" : len(all_users)}), 200)
        return make_response(jsonify({"Status" : "NOT FOUND", "Message" : "The Database does not have any users"}), 404)

class Get_user_by_id(Resource):

    #Get user by Id
    def get(self, id):
        query = """ SELECT * FROM users WHERE id = %s """
        user = cur.execute(query, (id))
        if user:
            return make_response(jsonify({"Status" : "Ok", "Message" : "Successful", "user" : user}), 200)
        return make_response(jsonify({"Status" : "NOT FOUND", "Message" : "User does not exists"}), 200)

class Login(Resource):
    def post(self):
        user_info = request.get_json()

        username = user_info['username']
        password = user_info['password']

        response = users.login(username, password)
        if response == True:
            return make_response(jsonify({"Status" : "Ok", "Message" : "Successfully Logged in"}), 200)
        else:
            return make_response(jsonify({"Status" : "NOT FOUND", "Message" : response}), 404)


""" Routes for Products """

class Products(Resource):

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

    def get(self):
        response = products.get_all_products()

        if len(response) > 0:
            return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull", "Products" : response, "No Of products" : len(response)}), 200)
        else:
            return make_response(jsonify({"Status" : "NOT FOUND", "Message" : "The Database does not have products"}), 404)
        
        
    
