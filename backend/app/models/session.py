from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
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
    transcripts = relationship("Transcript", back_populates="session", cascade="all, delete-orphan")
    action_items = relationship("ActionItem", back_populates="session", cascade="all, delete-orphan")
    summaries = relationship("Summary", back_populates="session", cascade="all, delete-orphan")

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    content = Column(String, nullable=False)
    
    session = relationship("Session", back_populates="cards")

class Transcript(Base):
    __tablename__ = "transcripts"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    is_user = Column(Boolean, nullable=False)
    text = Column(String, nullable=False)

    session = relationship("Session", back_populates="transcripts")

class ActionItem(Base):
    __tablename__ = "action_items"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    text = Column(String, nullable=True)
    is_completed = Column(String, nullable=False)

    session = relationship("Session", back_populates="action_items")

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    text = Column(String, nullable=False)

    session = relationship("Session", back_populates="summaries")