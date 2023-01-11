import sys
from fastapi import Depends, FastAPI, Query, Request
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
    returned_products = []
    if category:
        products = products.filter(Product.category == category)
    if price_less_than:
        products = products.filter(Product.price_final <= price_less_than)
    for product in products:
        returned_products.append({
            "sku": product.sku,
            "name": product.name,
            "category": product.name,
            "price": {
                "original": product.price_original,
                "final":  product.price_original - (product.price_original * product.discount_percentage/100) if(product.discount_percentage != 0) else product.price_original,
                "discount_percentage": "null" if(product.discount_percentage == 0) else str(product.discount_percentage) +"%",
                "currency": "USD"
            }
        })
    return returned_products

@app.post("/add")
async def add_product(product : Request, db: Session = Depends(get_db)):
    req_info = await product.json()
    print("request info",req_info)
    name = req_info.get("name", None)
    category = req_info.get("category", None)
    sku = req_info.get("sku", None)
    price_original = req_info.get("price_original", None)
    discount_percentage = req_info.get("discount_percentage", None)
    try:
        product = Product(name=name,category=category,sku=sku,price_original=price_original,discount_percentage=discount_percentage)
        db.add(product)
        db.commit()

        return {"success" : True}
    
    except:
        db.rollback()
        print(sys.exc_info())
        return {"success" : False}
    
    finally:
        db.close()


