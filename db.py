from sqlalchemy import create_engine
import os
from models import Base,os
from sqlalchemy.orm import Session

DATABASE_URL = os.environ['DATABASE_URL']

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

def get_db():
    connection = engine.connect()
    session = Session(bind=connection)
    return session