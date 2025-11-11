from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    
    mentor_id = Column(Integer, ForeignKey("mentors.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    mentor = relationship("Mentor", back_populates="sessions")
    user = relationship("User", back_populates="sessions")
    cards = relationship("Card", back_populates="session", cascade="all, delete-orphan")

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    content = Column(String, nullable=False)
    
    session = relationship("Session", back_populates="cards")