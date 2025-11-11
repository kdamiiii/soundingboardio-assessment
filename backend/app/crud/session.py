from sqlalchemy.orm import Session
from app.models.session import Session, Card
from app.schemas.session import SessionCreate
from app.schemas.card import CardCreate

def create_session(db: Session, session: SessionCreate, user_id: int):
    db_session = Session(
        mentor_id=session.mentor_id,
        user_id=user_id
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def get_sessions(db: Session, user_id:int = None):
    print(user_id)
    if user_id is not None:
        return db.query(Session).filter(Session.user_id == user_id).all()
    return db.query(Session).all()

def get_session_by_id(db: Session, session_id: int):
    return db.query(Session).filter(Session.id == session_id).first()