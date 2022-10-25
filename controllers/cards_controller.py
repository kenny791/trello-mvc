from datetime import date
from time import time
from flask import Blueprint, request
from db import db
from models.card import Card, CardSchema

cards_bp = Blueprint('cards', __name__, url_prefix='/cards')

@cards_bp.route('/')
# @jwt_required()
def all_cards():
    # return 'All cards'
    # if not authorize():
    #     return {'error': 'You must be an admin'}, 401
    stmt = db.select(Card).order_by(Card.priority.desc(), Card.title)
    cards = db.session.scalars(stmt)
    return CardSchema(many=True).dump(cards)

@cards_bp.route('/<int:id>/')
def one_card(id):
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)
    if card:
        return CardSchema().dump(card)
    else:
        return {'error': f'Card not found with id {id}'}, 404

@cards_bp.route('/', methods=['POST'])
def create_card():
    #Create a new Card model instance
    card = Card(
        title=request.json['title'],
        description=request.json['description'],
        date=date.today(),
        status=request.json['status'],
        priority=request.json['priority']
    )
    #Add and commit user to DB
    db.session.add(card)
    db.session.commit()
    #Respond to client
    return CardSchema().dump(card),201