from pydantic import BaseModel

class TranscriptBase(BaseModel):
    text: str
    is_user: bool

class TranscriptCreate(TranscriptBase):
    pass

class TranscriptOut(TranscriptBase):
    id: int
    
    model_config = {"from_attributes": True}

class TranscriptOutWithSession(TranscriptOut):
    session_id: int