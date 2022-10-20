from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.cards_controller import cards_bp
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    db.init_app(app)

    app.register_blueprint(cards_bp)

    return app


