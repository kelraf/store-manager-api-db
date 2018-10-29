import os
from flask import Flask, Blueprint
from flask_restful import Api
from instance.config import app_config
from manage import DatabaseSetup

application_bp = Blueprint("application_bp", __name__, url_prefix="/api/v2")
api = Api(application_bp)

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config['development'])
    app.secret_key = os.getenv('SECRET_KEY')

    setup = DatabaseSetup()
    setup.create_tables()
    app.register_blueprint(application_bp)
    return app