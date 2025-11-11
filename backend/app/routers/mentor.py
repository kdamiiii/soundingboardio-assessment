from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.mentor import get_mentor_by_id, get_mentors, create_mentor, update_mentor, delete_mentor
from app.schemas.mentor import MentorOut, MentorCreate, MentorUpdate

router = APIRouter(prefix="/mentors", tags=["mentors"])

@router.get("/", response_model=list[MentorOut])
def read_mentors(db: Session = Depends(get_db)):
    return get_mentors(db)

@router.post("/", response_model=MentorOut)
def post_mentor(user: MentorCreate, db: Session = Depends(get_db)):
    return create_mentor(db, user)

@router.get("/{mentor_id}/", response_model=MentorOut)
def read_mentor(mentor_id: int, db: Session = Depends(get_db)):
    return get_mentor_by_id(db, mentor_id)

@router.patch("/{mentor_id}/", response_model=MentorUpdate)
def patch_mentor(mentor_id: int, mentor_update: MentorUpdate, db: Session = Depends(get_db)):
    return update_mentor(db, mentor_id, mentor_update)

@router.delete("/{mentor_id}/", response_model=dict)
def del_mentor(mentor_id: int, db: Session = Depends(get_db)):
    delete_mentor(db, mentor_id)
    return {"detail": "Mentor deleted"}