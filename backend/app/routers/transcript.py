from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.transcript import get_transcripts
from app.schemas.transcript import TranscriptOutWithSession

router = APIRouter(prefix="/transcripts", tags=["transcripts"])

@router.get("/", response_model=list[TranscriptOutWithSession])
def read_transcripts(db: Session = Depends(get_db)):
    return get_transcripts(db)