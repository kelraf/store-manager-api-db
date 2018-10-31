import os
from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager

#Local imports
from instance.config import app_config
from manage import DatabaseSetup
from app.api.v2.views import Users, Get_user_by_id, Login, Products, Get_product_by_id, Sales

application_bp = Blueprint("application_bp", __name__, url_prefix="/api/v2")
api = Api(application_bp)

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config['development'])
    app.config['JWT_SECRET_KEY'] = "rafkelrafxxxxxx-xxxxxx-xxxxx"
    jwt = JWTManager(app)
    app.secret_key = os.getenv('SECRET_KEY')

    setup = DatabaseSetup()
    setup.create_tables()
    app.register_blueprint(application_bp)

    api.add_resource(Users, "/register")
    api.add_resource(Get_user_by_id, "/register/<int:id>")
    api.add_resource(Login, "/login")

    #Product resources
    api.add_resource(Products, "/products")
    api.add_resource(Get_product_by_id, "/products/<int:id>")

    #Sales resources
    api.add_resource(Sales, "/sales")
    return app