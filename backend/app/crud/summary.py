from sqlalchemy.orm import Session
from app.models.session import Summary
from app.schemas.summary import SummaryCreate

def get_summaries(db: Session):
    return db.query(Summary).all()

def get_summaries_by_session_id(db: Session, session_id: int):
    return db.query(Summary).filter(Summary.session_id == session_id).all()

def create_summary(db: Session, session_id:int, summary: SummaryCreate):
    db_summary = Summary(
        session_id=session_id,
        text=summary.text
    )
    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)

    return db_summary
