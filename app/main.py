from fastapi import FastAPI
from app.routers import words
from app.database.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vocabulary API", version="1.0")

app.include_router(words.router)

