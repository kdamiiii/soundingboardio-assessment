from pydantic import BaseModel

class SummaryBase(BaseModel):
    text: str

class SummaryCreate(SummaryBase):
    pass

class SummaryOut(SummaryBase):
    id: int
    
    model_config = {"from_attributes": True}

class SummaryOutWithSession(SummaryOut):
    session_id: int