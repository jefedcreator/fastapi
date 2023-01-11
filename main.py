import sys
from fastapi import Depends, FastAPI, Query, Request
from sqlalchemy.orm import Session
from models import Product, Discount
from typing import Optional
from db import get_db
from service import DiscountService
app = FastAPI()

@app.get("/products")
async def get_products(
    category: Optional[str] = Query(None, alias="category"),
    price_less_than: Optional[float] = Query(None, alias="price_less_than"),
    db: Session = Depends(get_db),
):
    products = db.query(Product).all()
    discounts = db.query(Discount).all()
    returned_products = []
    if category:
        products = products.filter(Product.category == category)
    if price_less_than:
        products = products.filter(Product.price <= price_less_than)

    discounted_products = DiscountService.apply_discounts(products=products,discounts=discounts)
    return discounted_products

@app.post("/discounts")
async def add_discount(product : Request, db: Session = Depends(get_db)):
    req_info = await product.json()
    category = req_info.get("category", None)
    sku = req_info.get("sku", None)
    percentage = req_info.get("percentage", None)
    try:
        discount =  Discount(category=category,sku=sku,percentage=percentage)
        db.add(discount)
        db.commit()

        return {"success" : True}
    
    except:
        db.rollback()
        print(sys.exc_info())
        return {"success" : False}
    
    finally:
        db.close()


