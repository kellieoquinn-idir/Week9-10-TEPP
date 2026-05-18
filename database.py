#This is for my database connection
#This file will handle the connection to the database. In this case, it's a SQLite DB. Nothing crazy.
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import DBModelBase

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'test.db'}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)