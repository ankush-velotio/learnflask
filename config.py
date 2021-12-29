import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False

    TESTING = False

    CSRF_ENABLED = True

    # Secret key for signing cookies
    SECRET_KEY = "57e19ea558d4967a552d03deece34a70"

    # Secret key for signing the data.
    CSRF_SESSION_KEY = "secret"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2


class ProductionConfig(Config):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevelopmentConfig(Config):
    DEBUG = True

    # Define the database
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.db")

    ENV = "development"

    DEVELOPMENT = True
