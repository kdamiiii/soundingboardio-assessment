from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.user import get_users, create_user
from app.schemas import user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[user.UserOut])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/", response_model=user.UserOut)
def post_user(user: user.UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)