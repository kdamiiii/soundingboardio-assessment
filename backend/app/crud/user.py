from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.user import UserCreate, UserUpdate
from app.models.session import Session as SessionModel
from app.models.user import User
from app.exceptions import HttpException
from app.models.mentor import Mentor

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    try:
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HttpException(status_code=400, detail="User with this email already exists")
    except Exception as e:
        db.rollback()
        raise e
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def update_user(db: Session, user_id: int, user_data: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    update_data = user_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.email == username).first()
    if user and user.password == password:
        return user
    return None

def get_user_with_mentors(db: Session, user_id: int):
    results = (
        db.query(
            User.id.label("user_id"),
            User.first_name,
            User.last_name,
            User.email,
            Mentor.id.label("mentor_id"),
            Mentor.name.label("mentor_name"),
            Mentor.tags,
            Mentor.bio,
            Mentor.focus_areas,
            Mentor.about,
            Mentor.photo,
            Mentor.coach_introduction,
            func.count(SessionModel.id).label("session_count")
        )
        .join(SessionModel, SessionModel.user_id == User.id)
        .join(Mentor, SessionModel.mentor_id == Mentor.id)
        .filter(User.id == user_id)
        .group_by(User.id, Mentor.id)
        .all()
    )

    if not results:
        return None
    
    user_data = {
        "id": results[0].user_id,
        "first_name": results[0].first_name,
        "last_name": results[0].last_name,
        "email": results[0].email,
        "mentors": []
    }

    for row in results:
        user_data["mentors"].append({
            "id": row.mentor_id,
            "name": row.mentor_name,
            "tags": row.tags,
            "bio": row.bio,
            "focus_areas": row.focus_areas,
            "about": row.about,
            "photo": row.photo,
            "coach_introduction": row.coach_introduction,
            "session_count": row.session_count
        })

    return user_data