from flask import Flask

from auth.views import auth
from database import database


def create_app(test_config=None):
    app = Flask(__name__)
    # Setup with the provided configuration
    app.config.from_object("config.DevelopmentConfig")

    if test_config is not None:
        app.config.update(test_config)

    database.init_app(app)

    # register blueprints
    app.register_blueprint(auth)

    return app


if __name__ == "__main__":
    create_app().run()
