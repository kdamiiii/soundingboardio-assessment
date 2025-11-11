from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.transcript import get_transcript_by_id, get_transcripts, delete_transcript
from app.schemas.transcript import TranscriptOutWithSession

router = APIRouter(prefix="/transcripts", tags=["transcripts"])

@router.get("/", response_model=list[TranscriptOutWithSession])
def read_transcripts(db: Session = Depends(get_db)):
    return get_transcripts(db)

@router.get("/{transcript_id}/", response_model=TranscriptOutWithSession)
def read_transcript_by_id(transcript_id: int, db: Session = Depends(get_db)):
    return get_transcript_by_id(db, transcript_id)

@router.delete("/{transcript_id}/", response_model=dict)
def del_transcript(transcript_id: int, db: Session = Depends(get_db)):
    delete_transcript(db, transcript_id)
    return {"detail": "Transcript deleted"}