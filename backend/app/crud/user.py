from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.models import user as user_model

def get_users(db: Session):
    return db.query(user_model.User).all()

def create_user(db: Session, user: user_schema.UserCreate):
    db_user = user_model.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(user_model.User).filter(user_model.User.email == username).first()
    if user and user.password == password:
        return user
    return None