from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth import TokenData
from app.schemas.session import SessionDetailsOut, SessionOut, SessionCreate
from app.schemas.card import CardCreate, CardOut
from app.schemas.transcript import TranscriptCreate, TranscriptOut
from app.schemas.action_item import ActionItemCreate, ActionItemOut
from app.schemas.summary import SummaryCreate, SummaryOut
from app.dependencies.auth import get_current_user, get_current_user_optional
from app.crud.session import delete_session, get_session_by_id, get_sessions, create_session
from app.crud.card import create_card, get_cards_by_sesssion_id
from app.crud.transcript import create_transcript, get_transcripts_by_sesssion_id
from app.crud.action_item import create_action_item, get_action_items_by_session_id
from app.crud.summary import create_summary, get_summaries_by_session_id

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.get("/", response_model=list[SessionOut])
def read_sessions(db: Session = Depends(get_db), current_user: Optional[TokenData] = Depends(get_current_user_optional)):
    return get_sessions(db, current_user.user_id if current_user else None)

@router.get("/{session_id}/", response_model=SessionDetailsOut)
def read_session_by_id(session_id: int, db: Session = Depends(get_db)):
    session = get_session_by_id(db, session_id)
    return session

@router.get("/{session_id}/cards/", response_model=list[CardOut])
def read_cards(session_id: int, db: Session = Depends(get_db)):
    cards = get_cards_by_sesssion_id(db, session_id)
    return cards

@router.post("/{session_id}/cards/", response_model=CardOut)
def post_card_to_session(session_id: int, card_data:CardCreate, db: Session = Depends(get_db)):
    card = create_card(db, session_id, card_data)
    return card

@router.get("/{session_id}/transcripts/", response_model=list[TranscriptOut])
def read_transcripts(session_id: int, db: Session = Depends(get_db)):
    transcripts = get_transcripts_by_sesssion_id(db, session_id)
    return transcripts

@router.post("/{session_id}/transcripts/", response_model=TranscriptOut)
def post_transcript_to_session(session_id: int, card_data:TranscriptCreate, db: Session = Depends(get_db)):
    transcript = create_transcript(db, session_id, card_data)
    return transcript

@router.get("/{session_id}/action_items/", response_model=list[ActionItemOut])
def read_action_items(session_id: int, db: Session = Depends(get_db)):
    action_items = get_action_items_by_session_id(db, session_id)
    return action_items

@router.post("/{session_id}/action_items/", response_model=ActionItemOut)
def post_action_item_to_session(session_id: int, card_data:ActionItemCreate, db: Session = Depends(get_db)):
    action_item = create_action_item(db, session_id, card_data)
    return action_item

@router.get("/{session_id}/summaries/", response_model=list[SummaryOut])
def read_summary(session_id: int, db: Session = Depends(get_db)):
    summaries = get_summaries_by_session_id(db, session_id)
    return summaries

@router.post("/{session_id}/summaries/", response_model=SummaryOut)
def post_summary_to_session(session_id: int, card_data:SummaryCreate, db: Session = Depends(get_db)):
    summary = create_summary(db, session_id, card_data)
    return summary

@router.post("/", response_model=SessionOut)
def post_session(session: SessionCreate, db: Session = Depends(get_db), current_user:TokenData = Depends(get_current_user)):    
    return create_session(db, session, current_user.user_id)

@router.delete("/{session_id}/", response_model=dict)
def del_session(session_id: int, db: Session = Depends(get_db)):
    delete_session(db, session_id)
    return {"detail": "Session deleted"}