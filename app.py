from flask import Flask

from auth.views import auth
from database import database


def create_app():
    app = Flask(__name__)
    # Setup with the provided configuration
    app.config.from_object("config.DevelopmentConfig")

    database.init_app(app)

    # register blueprints
    app.register_blueprint(auth)

    return app


if __name__ == "__main__":
    create_app().run()
