from typing import List
from pydantic import BaseModel
from app.schemas.card import CardOut

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