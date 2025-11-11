from typing import Optional, List
from pydantic import BaseModel, EmailStr

from app.schemas.session import SessionDetailsOut
from app.schemas.mentor import MentorWithSessionCountOut

class UserBase(BaseModel):
    email: EmailStr
    first_name:str
    middle_name:Optional[str]= None
    last_name:str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

class UserDetailsOut(UserOut):
    sessions: list[SessionDetailsOut] = []

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None

class UserMentorsSessionsOut(UserOut):
    mentors: List[MentorWithSessionCountOut] = []