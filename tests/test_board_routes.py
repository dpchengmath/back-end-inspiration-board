from app.models.board import Board
import pytest


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_boards_no_saved_boards(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {'boards':[]}

# @pytest.mark.skip(reason="No way to test this feature yet")
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