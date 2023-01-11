from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

# models.py
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv

load_dotenv('.env')

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    sku = Column(String, index=True)
    price_original = Column(Float, index=True)
    discount_percentage = Column(Float, index=True)
    price_final = Column(Float, index=True)
    
    def __init__(self, name: str, category: str, price_original: float, discount_percentage: float, price_final:float):
        self.name = name
        self.category = category
        self.price_original = price_original
        self.discount_percentage = discount_percentage
        self.price_final = price_final

# database.py
from sqlalchemy import create_engine

DATABASE_URL = os.environ['DATABASE_URL']

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

def get_db():
    connection = engine.connect()
    session = Session(bind=connection)
    return session

# main.py
from typing import Optional

@app.get("/products")
async def get_products(
    category: Optional[str] = Query(None, alias="category"),
    price_less_than: Optional[float] = Query(None, alias="price_less_than"),
    db: Session = Depends(get_db),
):
    products = db.query(Product).all()
    if category:
        products = products.filter(Product.category == category)
    if price_less_than:
        products = products.filter(Product.price_final <= price_less_than)
    return products
