from flask import Flask
from app.controllers import post_controller


def create_app():
    app = Flask(__name__)

    post_controller.init_app(app)

    return app
