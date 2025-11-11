from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies.auth import get_current_user, get_current_user_optional
from app.crud.session import get_session_by_id, get_sessions, create_session
from app.crud.card import create_card, get_cards_by_sesssion_id
from app.schemas.auth import TokenData
from app.schemas.session import SessionDetailsOut, SessionOut, SessionCreate
from app.schemas.card import CardCreate, CardOut
from app.schemas.transcript import TranscriptCreate, TranscriptOut
from app.crud.transcript import create_transcript, get_transcripts_by_sesssion_id

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.get("/", response_model=list[SessionOut])
def read_sessions(db: Session = Depends(get_db), current_user: Optional[TokenData] = Depends(get_current_user_optional)):
    return get_sessions(db, current_user.user_id if current_user else None)

@router.get("/{session_id}/", response_model=SessionDetailsOut)
def read_session(session_id: int, db: Session = Depends(get_db)):
    session = get_session_by_id(db, session_id)
    return session

@router.get("/{session_id}/cards/", response_model=list[CardOut])
def read_session(session_id: int, db: Session = Depends(get_db)):
    session = get_cards_by_sesssion_id(db, session_id)
    return session

@router.post("/{session_id}/cards/", response_model=CardOut)
def post_card_to_session(session_id: int, card_data:CardCreate, db: Session = Depends(get_db)):
    session = create_card(db, session_id, card_data)
    return session

@router.get("/{session_id}/transcripts/", response_model=list[TranscriptOut])
def read_session(session_id: int, db: Session = Depends(get_db)):
    session = get_transcripts_by_sesssion_id(db, session_id)
    return session

@router.post("/{session_id}/transcripts/", response_model=TranscriptOut)
def post_card_to_session(session_id: int, card_data:TranscriptCreate, db: Session = Depends(get_db)):
    session = create_transcript(db, session_id, card_data)
    return session

@router.post("/", response_model=SessionOut)
def post_session(session: SessionCreate, db: Session = Depends(get_db), current_user:TokenData = Depends(get_current_user)):    
    return create_session(db, session, current_user.user_id)
