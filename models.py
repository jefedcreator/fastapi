from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Discount(Base):
    __tablename__ = "discounts"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, index=True)
    category = Column(String, index=True)
    percentage = Column(Float)

    def __init__(self, sku=None, category=None, percentage=0):
        self.sku = sku
        self.category = category
        self.percentage = percentage
        
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)

    def __init__(self, args, sku, name, category, price):
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        for k in args:
            setattr(self, k, args[k])

    def __getitem__(self, item):
        return getattr(self, item)
