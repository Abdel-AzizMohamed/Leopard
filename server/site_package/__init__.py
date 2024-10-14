from flask import Flask
from flask_cors import CORS
from site_package.config import Config


def create_app(config=Config) -> Flask:
    """Creates a new flask app"""
    app = Flask(__name__)
    app.config.from_object(config)
    cors = CORS()
    cors.init_app(app)

    return app
