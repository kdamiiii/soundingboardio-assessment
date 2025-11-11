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

class MentorUpdate(BaseModel):
    name: Optional[str] = None
    tags: Optional[str] = None
    bio: Optional[str] = None
    focus_areas: Optional[str] = None
    about: Optional[str] = None
    photo: Optional[str] = None
    coach_introduction: Optional[str] = None

    model_config = {"from_attributes": True}

class MentorWithSessionCountOut(MentorOut):
    session_count: int