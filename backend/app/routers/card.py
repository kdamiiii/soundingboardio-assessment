from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.card import get_cards
from app.schemas.card import CardOutWithSession

router = APIRouter(prefix="/cards", tags=["cards"])

@router.get("/", response_model=list[CardOutWithSession])
def read_cards(db: Session = Depends(get_db)):
    return get_cards(db)