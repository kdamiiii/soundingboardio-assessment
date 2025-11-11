from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    
    mentor_id = Column(Integer, ForeignKey("mentors.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    mentor = relationship("Mentor", back_populates="sessions")
    user = relationship("User", back_populates="sessions")
    