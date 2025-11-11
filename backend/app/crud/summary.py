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

def get_summary_by_id(db: Session, summary_id: int):
    return db.query(Summary).filter(Summary.id == summary_id).first()

def delete_summary(db: Session, summary_id: int):
    db_summary = db.query(Summary).filter(Summary.id == summary_id).first()
    if db_summary:
        db.delete(db_summary)
        db.commit()
    return db_summary
