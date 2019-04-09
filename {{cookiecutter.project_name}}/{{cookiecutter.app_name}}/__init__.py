import os

from flask import Flask
from peewee import DoesNotExist
from .main.views import main as main_blueprint
from .api import api as api_blueprint

from configs import config
from {{cookiecutter.app_name}}.extensions import db
from {{cookiecutter.app_name}}.utils import not_exist


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "development")
    app.config.from_object(config[env])
    db.init_app(app)
    app.register_error_handler(DoesNotExist, not_exist)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)
    return app
