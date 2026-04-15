from fastapi import FastAPI
from app.routers import words
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Vocabulary API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(words.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Vocabulary API!"}