from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import user, mentor, session, auth
from app.routers import card

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SoundboardIO Assessment API")

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(mentor.router)
app.include_router(session.router)
app.include_router(card.router)