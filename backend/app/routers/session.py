from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.session import get_sessions, create_session
from app.schemas import session

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.get("/", response_model=list[session.SessionOut])
def read_sessions(db: Session = Depends(get_db)):
    return get_sessions(db)

@router.post("/", response_model=session.SessionOut)
def post_session(user: session.SessionCreate, db: Session = Depends(get_db)):
    return create_session(db, user)