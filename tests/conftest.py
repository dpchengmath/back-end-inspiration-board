import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.board import Board
from app.models.card import Card

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
     
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
    
@pytest.fixture
def one_board():
    new_board = Board(title = "Complete this project on time", 
                        owner = "Ada")
    db.session.add(new_board)
    db.session.commit()
    return new_board

@pytest.fixture
def three_cards(app):
    db.session.add_all([
        Card(message="Think of what you have succeeded in", 
             likes_count="3"),
        Card(message="Keep going, you're doing great", 
             likes_count="5"),
        Card(message="Do not give up, you're almost there", 
             likes_count="7")
    ])
    db.session.commit()


@pytest.fixture
def liked_card(app):
    new_card = Card(message="Go on my daily walk 🏞", 
                    likes_count="0")

    db.session.add(new_card)
    db.session.commit()

    