from typing import List
from pydantic import BaseModel
from app.schemas.card import CardOut
from app.schemas.transcript import TranscriptOut
from app.schemas.action_item import ActionItemOut
from app.schemas.summary import SummaryOut

class SessionBase(BaseModel):
    mentor_id: int

class SessionCreate(SessionBase):
    pass

class SessionOut(SessionBase):
    id: int
    user_id: int
    mentor_id: int
    
    model_config = {
        "from_attributes": True
    }

class SessionDetailsOut(SessionOut):
    cards: List[CardOut] = []
    transcripts: List[TranscriptOut] = []
    action_items: List[ActionItemOut] = []
    summaries: List[SummaryOut] = []