from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.summary import get_summaries
from app.schemas.summary import SummaryOutWithSession

router = APIRouter(prefix="/summaries", tags=["summaries"])

@router.get("/", response_model=list[SummaryOutWithSession])
def read_summaries(db: Session = Depends(get_db)):
    return get_summaries(db)