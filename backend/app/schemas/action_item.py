from pydantic import BaseModel

class ActionItemBase(BaseModel):
    text: str
    is_completed: bool

class ActionItemCreate(ActionItemBase):
    pass

class ActionItemOut(ActionItemBase):
    id: int
    
    model_config = {"from_attributes": True}

class ActionItemOutWithSession(ActionItemOut):
    session_id: int