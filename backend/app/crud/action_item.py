from sqlalchemy.orm import Session
from app.models.session import ActionItem
from app.schemas.action_item import ActionItemCreate

def get_action_items(db: Session):
    return db.query(ActionItem).all()

def get_action_items_by_session_id(db: Session, session_id: int):
    return db.query(ActionItem).filter(ActionItem.session_id == session_id).all()

def create_action_item(db: Session, session_id:int, action_item: ActionItemCreate):
    db_action_item = ActionItem(
        session_id=session_id,
        text=action_item.text,
        is_completed=action_item.is_completed
    )
    db.add(db_action_item)
    db.commit()
    db.refresh(db_action_item)

    return db_action_item

def mark_action_item_completed(db: Session, action_item_id: int):
    action_item = db.query(ActionItem).filter(ActionItem.id == action_item_id).first()
    if action_item:
        action_item.is_completed = True
        db.commit()
        db.refresh(action_item)
    return action_item

def get_action_item_by_id(db: Session, action_item_id: int):
    return db.query(ActionItem).filter(ActionItem.id == action_item_id).first()

def delete_action_item(db: Session, action_item_id: int):
    db_action_item = db.query(ActionItem).filter(ActionItem.id == action_item_id).first()
    if db_action_item:
        db.delete(db_action_item)
        db.commit()
    return db_action_item