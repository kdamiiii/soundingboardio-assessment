from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.mentor import get_mentors, create_mentor
from app.schemas import mentor

router = APIRouter(prefix="/mentors", tags=["mentors"])

@router.get("/", response_model=list[mentor.MentorOut])
def read_mentors(db: Session = Depends(get_db)):
    return get_mentors(db)

@router.post("/", response_model=mentor.MentorOut)
def post_mentor(user: mentor.MentorCreate, db: Session = Depends(get_db)):
    return create_mentor(db, user)