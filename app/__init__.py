import os
from flask import Flask, Blueprint
from flask_restful import Api
from instance.config import app_config
from manage import DatabaseSetup
from app.api.v2.views import Users, Get_user_by_id, Login, Products

application_bp = Blueprint("application_bp", __name__, url_prefix="/api/v2")
api = Api(application_bp)

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config['development'])
    app.secret_key = os.getenv('SECRET_KEY')

    setup = DatabaseSetup()
    setup.create_tables()
    app.register_blueprint(application_bp)

    api.add_resource(Users, "/register")
    api.add_resource(Get_user_by_id, "/register/<id>")
    api.add_resource(Login, "/login")

    api.add_resource(Products, "/products")
    return app



    #A dictionary to store user info before they can be stored in the database
        # user_info = {}

        # user_info['username']
        # user_info['email']
        # user_info['phone_number']
        # user_info['password']
        # user_info['confirm_password']