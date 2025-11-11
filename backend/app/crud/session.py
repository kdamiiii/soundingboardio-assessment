from sqlalchemy.orm import Session
from app.models import session as session_model
from app.schemas import session as session_schema

def get_sessions(db: Session):
    return db.query(session_model.Session).all()

def create_session(db: Session, session: session_schema.SessionCreate, user_id: int):
    db_session = session_model.Session(
        mentor_id=session.mentor_id,
        user_id=user_id
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session
