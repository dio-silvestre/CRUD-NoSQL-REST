from flask import Flask
from app.views import post_view


def create_app():
    app = Flask(__name__)

    post_view.init_app(app)

    return app
