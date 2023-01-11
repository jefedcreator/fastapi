from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session
from models import Product
from typing import Optional
from db import get_db
app = FastAPI()

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
