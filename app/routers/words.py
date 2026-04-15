from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.words import Vocabulary
from app.schemas.words import WordCreate, WordUpdate, AssetUpdate, WordResponse
from uuid import UUID


router = APIRouter(prefix="/v1", tags=["words"])


@router.post("/vocabulary", response_model=WordResponse)
async def create_word(word: WordCreate, db: Session = Depends(get_db)):
    db_word = Vocabulary(
        english_word=word.english_word,
        part_of_speech=word.part_of_speech,
        phonetic_transcription=word.phonetic_transcription,
        telegram_file_id=word.telegram_file_id,
        raw_storage_url=word.raw_storage_url,
        level=word.level,
        difficulty=word.difficulty
    )
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word

@router.get("/vocabulary/{word_id}", response_model=WordResponse)
async def get_word(word_id: UUID, db: Session = Depends(get_db)):
    word = db.query(Vocabulary).filter(Vocabulary.word_id == word_id).first()

    if not word:
        raise HTTPException(status_code=404, detail="Word not found")
    
    return word


@router.patch("/vocabulary/{word_id}", response_model=WordResponse)
async def update_word(word_id: UUID, word: WordUpdate, db: Session = Depends(get_db)):
    db_word = db.query(Vocabulary).filter(Vocabulary.word_id == word_id).first()

    if not db_word:
        raise HTTPException(status_code=404, detail="Word not found")

    for key, value in word.dict(exclude_unset=True).items():
        setattr(db_word, key, value)

    db.commit()
    db.refresh(db_word)
    return db_word

@router.patch("/vocabulary/{word_id}/assets", response_model=WordResponse)
async def update_word_assets(word_id: UUID, assets: AssetUpdate, db: Session = Depends(get_db)):
    db_word = db.query(Vocabulary).filter(Vocabulary.word_id == word_id).first()

    if not db_word:
        raise HTTPException(status_code=404, detail="Word not found")

    if assets.telegram_file_id is not None:
        db_word.telegram_file_id = assets.telegram_file_id

    db.commit()
    db.refresh(db_word)
    return db_word

@router.delete("/vocabulary/{word_id}")
async def delete_word(word_id: UUID, db: Session = Depends(get_db)):
    db_word = db.query(Vocabulary).filter(Vocabulary.word_id == word_id).first()

    if not db_word:
        raise HTTPException(status_code=404, detail="Word not found")

    db_word.is_active = False
    db.commit()
    return {"detail": "Word deleted successfully"}