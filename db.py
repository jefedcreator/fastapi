from sqlalchemy import create_engine
import os
from models import Base
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv('.env')

DATABASE_URL = os.environ['DATABASE_URL']

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

def get_db():
    connection = engine.connect()
    session = Session(bind=connection)
    return session