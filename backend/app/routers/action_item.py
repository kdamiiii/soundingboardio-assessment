from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.action_item import get_action_items
from app.schemas.action_item import ActionItemOutWithSession

router = APIRouter(prefix="/action_items", tags=["action_items"])

@router.get("/", response_model=list[ActionItemOutWithSession])
def read_action_items(db: Session = Depends(get_db)):
    return get_action_items(db)