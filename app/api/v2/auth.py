import jwt, os, datetime
from flask import request, make_response, jsonify
from functools import wraps

secret_key = "os.getenv(SECRET_KEY)"

class Auth():

    @staticmethod
    def encode_token(username, admin):
        try:
            token = jwt.encode( {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 60),
            'username': username,
            'admin':admin
        }, secret_key)
            return token
        except Exception as e:
            return e 



    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, secret_key)
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again'
        except jwt.InvalidTokenError:
            return 'Invalid token.Try log in again'
    
    @staticmethod
    def admin_only(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            authentication_header = request.headers.get('Authorization')
            if not authentication_header:
                return make_response(jsonify({"Status" : "FORBIDDEN", "Message" : "Authentication Required"}), 403)
            if authentication_header:    
                token = authentication_header.split(" ")[1]
                if not token:
                    return make_response(jsonify({"Status" : "FORBIDDEN", "Message" : "Please Provide A Token"}), 403)
                    
                try:
                    identity = jwt.decode(token, secret_key, algorithms='HS256') 
                except jwt.ExpiredSignatureError:
                    return make_response(jsonify({"Message" : "Expired Signature Please log in again"}), 403)

                except jwt.InvalidTokenError:
                    return  make_response(jsonify({"Status" : "UNAUTHORIZED", "Message" : "Invalid Token"}), 401)                      
                    
                if identity:
                    if not identity["admin"]:
                        return make_response(jsonify({"Status" : "FORBIDDEN", "Message" : "Not Allowed!! Admin Only"}), 403)
            return f(*args, **kwargs)
        return decorated


    @staticmethod
    def token_required(t):
        @wraps(t)
        def decorated_token(*args, **kwargs):
            token = None
            authentication_header = request.headers.get('Authorization')
            if not authentication_header:
                return make_response(jsonify({"Status" : "FORBIDDEN", "Message" : "Authentication Required"}), 403)
            if authentication_header:    
                token = authentication_header.split(" ")[1]

                if not token:
                    return make_response(jsonify({"Status" : "FORBIDDEN", "Message" : "Please Provide A Token"}), 403)
                try:
                    identity = jwt.decode(token, secret_key, algorithms='HS256') 
                except jwt.ExpiredSignatureError:
                    return make_response(jsonify({"Message" : "Expired Signature Please log in again"}), 403)

                except jwt.InvalidTokenError:
                    return  make_response(jsonify({"Status" : "UNAUTHORIZED", "Message" : "Invalid Token"}), 401)                      
                    
                
            return t(*args, **kwargs)
        return decorated_token