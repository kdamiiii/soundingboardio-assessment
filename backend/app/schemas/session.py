from pydantic import BaseModel

class SessionBase(BaseModel):
    mentor_id: int

class SessionCreate(SessionBase):
    pass

class SessionOut(SessionBase):
    id: int
    user_id: int
    mentor_id: int
    
    model_config = {"from_attributes": True}