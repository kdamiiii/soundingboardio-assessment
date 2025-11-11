from sqlalchemy.orm import Session
from app.models.session import Transcript
from app.schemas.transcript import TranscriptCreate

def get_transcripts(db: Session):
    return db.query(Transcript).all()

def get_transcripts_by_sesssion_id(db: Session, session_id: int):
    return db.query(Transcript).filter(Transcript.session_id == session_id).all()

def create_transcript(db: Session, session_id:int, transcript: TranscriptCreate):
    db_transcript = Transcript(
        session_id=session_id,
        text=transcript.text,
        is_user=transcript.is_user
    )
    db.add(db_transcript)
    db.commit()
    db.refresh(db_transcript)

    return db_transcript
