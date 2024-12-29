from flask import Blueprint, abort, make_response, Response, request
import requests
from app.models.board import Board
from app.models.card import Card
from ..routes.route_utilities import validate_model, create_model
from ..db import db
import os


bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

@bp.delete("/<card_id>")
def delete_card(card_id):
    card = validate_model(Card, card_id)
    
    db.session.delete(card)
    db.session.commit()

    response = {"message":f"Card {card.card_id} {card.message} deleted successfully"}
    return response, 200

@bp.put("/<card_id>/liked")
def increase_card_like_count(card_id):
    card = validate_model(Card, card_id)
    card.likes_count += 1

    db.session.commit()

    return {"message": f"Card {card.card_id} {card.message} like count updated successfully"}, 200

@bp.put("/<card_id>/disliked")
def decrease_card_like_count(card_id):
    card = validate_model(Card, card_id)
    card.likes_count -= 1

    db.session.commit()

    return {"message": f"Card {card.card_id} {card.message} like count updated successfully"}, 200
