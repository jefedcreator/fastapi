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
    
    def __init__(self, name: str, category: str, sku : str, price_original: float, discount_percentage: float):
        self.name = name
        self.category = category
        self.price_original = price_original
        self.discount_percentage = discount_percentage
        self.sku = sku

