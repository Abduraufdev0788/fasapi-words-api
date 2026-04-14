import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  
    DRIVERNAME = os.getenv("DRIVERNAME")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    USERNAME = os.getenv("DB_USER")
    PASSWORD = os.getenv("PASSWORD")
    DATABASE = os.getenv("DATABASE")


config = Config()

print(config.USERNAME)