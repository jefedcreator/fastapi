from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base


Base  = declarative_base()

class Details(Base):
    __tablename__ = 'details'
    name  = Column(Text)
    sku = Column(Text, primary_key=True)
    price = Column(Integer)
    category = Column(Text)



