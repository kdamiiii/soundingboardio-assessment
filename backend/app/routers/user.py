from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.user import get_user_by_id, get_user_with_mentors, get_users, create_user, update_user,delete_user
from app.schemas.user import UserCreate, UserDetailsOut, UserMentorsSessionsOut, UserOut, UserUpdate
from app.schemas.mentor import MentorOut

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}/", response_model=UserDetailsOut)
def read_user_by_id(user_id:int, db: Session = Depends(get_db)):
    return get_user_by_id(db,user_id)

@router.post("/", response_model=UserOut)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.patch("/{user_id}/", response_model=UserOut)
def patch_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user)

@router.delete("/{user_id}/", response_model=dict)
def del_user(user_id: int, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return {"detail": "User deleted"}

@router.get("/{user_id}/sessions/", response_model=UserMentorsSessionsOut)
def read_user_sessions(user_id:int, db: Session = Depends(get_db)):
    user = get_user_with_mentors(db,user_id)
    if not user:
        return {"detail": "User not found"}
    return user