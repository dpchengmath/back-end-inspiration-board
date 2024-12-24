from flask import Blueprint, abort, make_response, Response, request
import requests
from app.models.board import Board
from ..db import db
import os


bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

@bp.get("")
def get_boards():
    boards = Board.query.all()
    return {"boards": [board.to_dict()for board in boards]}