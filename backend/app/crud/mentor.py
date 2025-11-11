from sqlalchemy.orm import Session
from app.models import mentor as mentor_model
from app.schemas import mentor as mentor_schema

def get_mentors(db: Session):
    return db.query(mentor_model.Mentor).all()

def create_mentor(db: Session, mentor: mentor_schema.MentorCreate):
    db_mentor = mentor_model.Mentor(
        name=mentor.name,
        bio=mentor.bio,
        focus_areas=mentor.focus_areas,
        about=mentor.about,
        photo=mentor.photo,
        coach_introduction=mentor.coach_introduction
    )
    db.add(db_mentor)
    db.commit()
    db.refresh(db_mentor)
    return db_mentor
