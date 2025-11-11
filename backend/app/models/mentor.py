from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Mentor(Base):
    __tablename__ = "mentors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    tags = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    focus_areas = Column(String, nullable=True)
    about = Column(String, nullable=True)
    photo = Column(String, nullable=True)
    coach_introduction = Column(String, nullable=True)