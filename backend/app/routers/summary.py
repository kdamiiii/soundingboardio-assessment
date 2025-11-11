from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud.summary import get_summaries, get_summary_by_id, delete_summary
from app.schemas.summary import SummaryOutWithSession

router = APIRouter(prefix="/summaries", tags=["summaries"])

@router.get("/", response_model=list[SummaryOutWithSession])
def read_summaries(db: Session = Depends(get_db)):
    return get_summaries(db)

@router.get("/{summary_id}/", response_model=SummaryOutWithSession)
def read_summary_by_id(summary_id: int, db: Session = Depends(get_db)):
    return get_summary_by_id(db, summary_id)

@router.delete("/{summary_id}/", response_model=dict)
def del_summary(summary_id: int, db: Session = Depends(get_db)):
    delete_summary(db, summary_id)
    return {"detail": "Summary deleted"}