from app.db import get_db, close_db
from flask import Flask
import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = f"sqlite:///{BASEDIR}/data.db"
SECRET_KEY = "dev"


def create_app():
    """
    Creates the flask application. Assigns secret keys and stops sqlalchemy tracking notifications as this is
    inefficient.
    """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    return app
