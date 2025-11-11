from typing import Optional
from pydantic import BaseModel, EmailStr

from app.schemas.session import SessionDetailsOut

class UserBase(BaseModel):
    email: EmailStr
    first_name:str
    middle_name:Optional[str]= None
    last_name:str
    password: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    model_config = {"from_attributes": True}

class UserDetailsOut(UserOut):
    sessions: list[SessionDetailsOut] = []

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None