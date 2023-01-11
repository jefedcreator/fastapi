import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Details as ModelDetails

import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/", status_code=200)
async def home():
    return {"message": "hello world"}

@app.get('/all/{attribute}/', status_code=200)
async def get_products(attribute :int | str):
    categories = []
    if type(attribute) is str:
        categories = db.session.query(ModelDetails).filter(ModelDetails.category==attribute).all()
    if type(attribute) is int:
        categories = db.session.query(ModelDetails).filter(ModelDetails.price <= int(attribute)).all()
    if len(categories) == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    new_categories = []
    for category in categories:
        new_categories.append({
            "sku": category.sku,
            "name": category.name,
            "category": category.category,
            "price": {
                "original" : category.price,
                "final": category.price - (category.price * category.discount/100) if (category.discount) else category.price,
                "discount_percentage": str(category.discount) + "%" if(category.discount) else str(0) + "%",
                "currency": "USD"
            }
        }) 
    return new_categories




# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)