from flask import Blueprint, abort, make_response, Response, request
import requests
from app.models.board import Board
from app.models.card import Card
from .route_utilities import validate_model, create_model
from ..db import db
import os


bp = Blueprint("boards_bp", __name__, url_prefix="/boards")


@bp.get("")
def get_boards():
    boards = Board.query.all()
    return {"boards": [board.to_dict()for board in boards]}

@bp.get("/<board_id>")
def get_board(board_id):
    board = validate_model(Board, board_id)
    return {"boards": board.to_dict()}

@bp.get("/<board_id>/cards")
def get_cards_by_board(board_id):
    board = validate_model(Board,board_id)
    return {"cards": [card.to_dict() for card in board.cards]}

@bp.post("")
def create_board():
    request_body = request.get_json()
    
    board_data = {"title": request_body.get("title"), 
                 "owner": request_body.get("owner")}

    board_dict, status_code = create_model(Board, board_data)
    return {"board": board_dict}, status_code

@bp.post("/<board_id>/cards")
def create_associated_card_with_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    cards_ids = request_body.get("cards_ids", [])

    for card_id in cards_ids:
        card = validate_model(Card, card_id)
        card.board_id = board.board_id

    db.session.commit()

    return {
        "board_id": board.board_id,
        "cards_ids": cards_ids
    }, 200

