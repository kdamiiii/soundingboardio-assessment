from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import user, mentor, session, auth,card,transcript,summary
from app.routers import action_item

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SoundboardIO Assessment API")

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(mentor.router)
app.include_router(session.router)
app.include_router(card.router)
app.include_router(transcript.router)
app.include_router(action_item.router)
app.include_router(summary.router)