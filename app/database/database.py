from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import config

BASE_URL = URL.create(
    drivername=config.DRIVERNAME,
    username=config.USERNAME,
    password=config.PASSWORD,
    host=config.HOST,
    port=config.PORT,
    database=config.DATABASE,
)
engine = create_engine(BASE_URL)
SessionLocal = sessionmaker( bind=engine)
Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
