from app.models.board import Board
from app import db, create_app
import pytest


def test_get_boards_no_saved_boards(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {'boards':[]}

def test_get_boards_one_saved_board(client, one_board):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == {"boards" : [
        {
            "board_id": 1,
            "title": "Complete this project on time",
            "owner": "Ada"
        }
    ]}

def test_get_board(client, one_board):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "boards" in response_body
    assert response_body == {
        "boards": {
            "board_id": 1,
            "title": "Complete this project on time",
            "owner": "Ada"
        }
    }


def test_get_board_not_found(client):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Board 1 not found"}


def test_get_cards_for_specific_goal_no_cards(client, one_board):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "cards" in response_body
    assert len(response_body["cards"]) == 0
    assert response_body == {
        
        "cards": []
    }

def test_delete_board(client, one_board):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "message" in response_body
    assert response_body == {
        "message": 'Board 1 Complete this project on time deleted successfully'
    }
    assert db.session.get(Board, 1) == None
