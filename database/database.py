from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy object
db = SQLAlchemy()


def init_app(app):
    # Initialize SQLAlchemy object
    db.init_app(app)
    # Create all the database tables from all the models.py files inside blueprints or apps
    db.create_all(app=app)
