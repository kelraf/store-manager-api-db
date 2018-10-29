from flask import jsonify, make_response, request
from flask_restful import Resource

class Users(Resource):
    def post(self):
        return make_response(jsonify({"Status" : "Ok", "Message" : "User Registered Successfully"}), 201)

    def get(self):
        return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull"}), 200)

class Get_user_by_id(Resource):

    #Get user by Id
    def get(self):
        return make_response(jsonify({"Status" : "Ok", "Message" : "Successful"}), 201)

class Login(Resource):
    def post(self):
        return make_response(jsonify({"Status" : "Ok", "Message" : "Successfull"}), 200)
        
        
    
