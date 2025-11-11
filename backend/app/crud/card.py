from sqlalchemy.orm import Session
from app.models.session import Card
from app.schemas.card import CardCreate
from app.exceptions import DoesNotExistError

def get_cards(db: Session):
    return db.query(Card).all()

def get_cards_by_sesssion_id(db: Session, session_id: int):
    return db.query(Card).filter(Card.session_id == session_id).all()

def create_card(db: Session, session_id:int, card: CardCreate):
    db_card = Card(
        session_id=session_id,
        content=card.content
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)

    return db_card

def get_card_by_id(db: Session, card_id: int):
    card = db.query(Card).filter(Card.id == card_id).first()
    if not card:
        raise DoesNotExistError("Card not found")
    return card

def delete_card(db: Session, card_id: int):
    db_card = db.query(Card).filter(Card.id == card_id).first()
    if not db_card:
        raise DoesNotExistError("Card not found")
    db.delete(db_card)
    db.commit()
    return db_card
