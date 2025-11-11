from pydantic import BaseModel

class CardBase(BaseModel):
    content: str

class CardCreate(CardBase):
    pass

class CardOut(CardBase):
    id: int
    
    model_config = {"from_attributes": True}

class CardOutWithSession(CardOut):
    session_id: int