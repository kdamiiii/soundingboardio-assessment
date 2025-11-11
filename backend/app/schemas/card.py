from pydantic import BaseModel

class CardBase(BaseModel):
    content: str

class CardCreate(CardBase):
    pass

class CardOut(CardBase):
    id: int
    session_id: int
    
    model_config = {"from_attributes": True}