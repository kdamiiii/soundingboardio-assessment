from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.action_item import get_action_items, get_action_item_by_id, delete_action_item
from app.schemas.action_item import ActionItemOutWithSession

router = APIRouter(prefix="/action_items", tags=["action_items"])

@router.get("/", response_model=list[ActionItemOutWithSession])
def read_action_items(db: Session = Depends(get_db)):
    return get_action_items(db)

@router.get("/{action_item_id}/", response_model=ActionItemOutWithSession)
def read_action_item_by_id(action_item_id: int, db: Session = Depends(get_db)):
    return get_action_item_by_id(db, action_item_id)

@router.delete("/{action_item_id}/", response_model=dict)
def del_action_item(action_item_id: int, db: Session = Depends(get_db)):
    delete_action_item(db, action_item_id)
    return {"detail": "Action item deleted"}