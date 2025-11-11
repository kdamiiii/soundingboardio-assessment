from pydantic import BaseModel
from typing import Optional

class MentorBase(BaseModel):
    name:str
    tags:Optional[str]
    bio:Optional[str]
    focus_areas:Optional[str]
    about:Optional[str]
    photo:Optional[str]
    coach_introduction:Optional[str]

class MentorCreate(MentorBase):
    pass

class MentorOut(MentorBase):
    id: int

    model_config = {"from_attributes": True}