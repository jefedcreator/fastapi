import sys
from fastapi import Depends, FastAPI, Query, Request
from sqlalchemy.orm import Session
from models import Product, Discount
from typing import Optional
from db import get_db
from service import ProductService
app = FastAPI()

@app.get("/products")
async def get_products(
    category: Optional[str] = Query(None, alias="category"),
    price_less_than: Optional[int] = Query(None, alias="price_less_than"),
    db: Session = Depends(get_db),
):
    products = db.query(Product).all()
    discounts = db.query(Discount).all()
    if category:
        products = ProductService.filter_products_by_category(products=products,query=category)
    if price_less_than:
        products = ProductService.filter_products_by_price(products=products,query=price_less_than)
    if category and price_less_than:
        products = ProductService.filter_products_by_category(products=products,query=category) +  ProductService.filter_products_by_price(products=products,query=price_less_than)

    discounted_products = ProductService.apply_discounts(products=products,discounts=discounts)
    return discounted_products

@app.post("/discounts")
async def add_discount(discount : Request, db: Session = Depends(get_db)):
    req_info = await discount.json()
    category = req_info.get("category", None)
    sku = req_info.get("sku", None)
    percentage = req_info.get("percentage", 0)
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

#testing purposes
@app.post("/products")
async def add_discount(product : Request, db: Session = Depends(get_db)):
    req_info = await product.json()
    category = req_info.get("category", None)
    sku = req_info.get("sku", None)
    name = req_info.get("name", None)
    price = req_info.get("price", None)
    try:
        discount =  Product(category=category,sku=sku,name=name,price=price)
        db.add(discount)
        db.commit()

        return {"success" : True}
    
    except:
        db.rollback()
        print(sys.exc_info())
        return {"success" : False}
    
    finally:
        db.close()


