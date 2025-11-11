from sqlalchemy.orm import Session
from app.models.session import Transcript
from app.schemas.transcript import TranscriptCreate
from app.exceptions import DoesNotExistError

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

def delete_transcript(db: Session, transcript_id: int):
    db_transcript = db.query(Transcript).filter(Transcript.id == transcript_id).first()
    if not db_transcript:
        raise DoesNotExistError("Transcript not found")
    db.delete(db_transcript)
    db.commit()
    return db_transcript

def get_transcript_by_id(db: Session, transcript_id: int):
    transcript = db.query(Transcript).filter(Transcript.id == transcript_id).first()

    if not transcript:
        raise DoesNotExistError("Transcript not found")
    
    return transcript