from sqlalchemy.orm import Session
from app.models.mentor import Mentor
from app.schemas.mentor import MentorCreate, MentorUpdate

def get_mentors(db: Session):
    return db.query(Mentor).all()

def create_mentor(db: Session, mentor: MentorCreate):
    db_mentor = Mentor(**mentor.model_dump())
    db.add(db_mentor)
    db.commit()
    db.refresh(db_mentor)
    return db_mentor

def get_mentor_by_id(db: Session, mentor_id: int):
    return db.query(Mentor).filter(Mentor.id == mentor_id).first()

def update_mentor(db: Session, mentor_id: int, mentor_update: MentorUpdate):
    db_mentor = db.query(Mentor).filter(Mentor.id == mentor_id).first()
    if not db_mentor:
        return None

    update_data = mentor_update.model_dump(exclude_unset=True)
    for var, value in update_data.items():
        setattr(db_mentor, var, value)

    db.commit()
    db.refresh(db_mentor)
    return db_mentor

def delete_mentor(db: Session, mentor_id: int):
    db_mentor = db.query(Mentor).filter(Mentor.id == mentor_id).first()
    if db_mentor:
        db.delete(db_mentor)
        db.commit()
    return db_mentor