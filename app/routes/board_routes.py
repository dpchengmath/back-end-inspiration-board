from flask import Blueprint, abort, make_response, Response, request
import requests
from app.models.board import Board
from .route_utilities import validate_model
from ..db import db
import os


bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

@bp.get("")
def get_boards():
    boards = Board.query.all()
    return {"boards": [board.to_dict()for board in boards]}


@bp.get("/<board_id>/cards")
def get_cards_by_board(board_id):
    board = validate_model(Board,board_id)
    return {"cards": [card.to_dict() for card in board.cards]}