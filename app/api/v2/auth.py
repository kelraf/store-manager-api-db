import jwt, os, datetime
from flask import request
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
                return "Authentication Required"
            if authentication_header:    
                try:
                    token = authentication_header.split(" ")[1]
                        
                    identity = jwt.decode(token, secret_key)                 

                except Exception:
                    return  'You are not authorized'
                       
                    
                if token:
                    if identity["admin"] == False:
                        return "Not Allowed!! Admin Only"
            return f(*args, **kwargs)
        return decorated


    @staticmethod
    def token_required(t):
        @wraps(t)
        def decorated_token(*args, **kwargs):
            token = None
            authentication_header = request.headers.get('Authorization')
            if not authentication_header:
                return "Authentication Required"
            if authentication_header:    
                try:
                    token = authentication_header.split(" ")[1]

                    if token:
                        identity = jwt.decode(token, secret_key)
                    else:
                        return "Token Required"
                except Exception:
                    return 'Token Required'
            return t(*args, **kwargs)
        return decorated_token