from flask import Flask
from flask_cors import CORS
from .db import db, migrate
from .models.board import Board
from .models.card import Card
from .routes.board_routes import bp as boards_bp
from .routes.card_routes import bp as cards_bp
import os
from flask_cors import CORS
# Import models, blueprints, and anything else needed to set up the app or database

def create_app(config=None):
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)

    # Initialize app with SQLAlchemy db and Migrate

    # Register Blueprints
    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(boards_bp)
    app.register_blueprint(cards_bp)
    return app
