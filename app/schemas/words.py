from pydantic import BaseModel
from uuid import UUID


class WordCreate(BaseModel):
    english_word : str
    part_of_speech : str | None = None
    raw_storage_url : str
    telegram_file_id : str
    phonetic_transcription : str | None = None
    level : str 
    difficulty : int


class WordUpdate(BaseModel):
    english_word : str | None = None
    part_of_speech : str | None = None
    level : str | None = None
    difficulty : int | None = None

class AssetUpdate(BaseModel):
    telegram_file_id : str


class WordResponse(BaseModel):
    word_id : UUID
    english_word : str
    part_of_speech : str | None = None
    raw_storage_url : str
    phonetic_transcription : str | None = None
    level : str 
    difficulty : int
    is_active : bool
    telegram_file_id : str

    class Config:
        from_attributes = True
