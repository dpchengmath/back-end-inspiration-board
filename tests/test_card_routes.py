from app.models.card import Card
from app import db, create_app
import pytest


def test_mark_liked_on_card(client, liked_card):
    # Act
    response = client.put("/cards/1/liked")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"message": f"Card 1 Go on my daily walk 🏞 like count updated successfully"}
    assert db.session.get(Card, 1).likes_count == 1