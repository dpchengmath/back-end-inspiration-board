from app.models.card import Card
from app.models.board import Board
from app import db, create_app
import pytest


def test_mark_liked_on_card(client, liked_card):
    # Act
    response = client.put("/cards/1/liked")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"message": f"Card 1 Small steps lead to big results like count updated successfully"}
    assert db.session.get(Card, 1).likes_count == 1

def test_mark_disliked_on_card(client, disliked_card):
    # Act
    response = client.put("/cards/1/disliked")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"message": f"Card 1 Small steps lead to big results like count updated successfully"}
    assert db.session.get(Card, 1).likes_count == 0

