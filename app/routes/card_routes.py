from flask import Blueprint, abort, make_response, Response, request
import requests
from app.models.board import Board
from ..db import db
import os


bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

