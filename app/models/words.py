from sqlalchemy import Column, String, Integer, Boolean
from app.database.database import Base

class Vocabulary(Base):
    __tablename__ = "vocabulary"
    word_id = Column(Integer, primary_key=True, index=True)
    english_word = Column(String, nullable=False)
    part_of_speech = Column(String, nullable=True)
    phonetic_transcription = Column(String, nullable=True)
    raw_storage_url = Column(String, nullable=False)
    telegram_file_id = Column(String, nullable=True)
    level = Column(String, nullable=False)
    difficulty = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)
