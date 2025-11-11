from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.card import get_cards, get_card_by_id, delete_card
from app.schemas.card import CardOutWithSession

router = APIRouter(prefix="/cards", tags=["cards"])

@router.get("/", response_model=list[CardOutWithSession])
def read_cards(db: Session = Depends(get_db)):
    return get_cards(db)

@router.get("/{card_id}/", response_model=CardOutWithSession)
def read_card_by_id(card_id: int, db: Session = Depends(get_db)):
    return get_card_by_id(db, card_id)

@router.delete("/{card_id}/", response_model=dict)
def del_card(card_id: int, db: Session = Depends(get_db)):
    delete_card(db, card_id)
    return {"detail": "Card deleted"}