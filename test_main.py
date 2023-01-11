from fastapi.testclient import TestClient
from fastapi import status
from main import app
import json

client = TestClient(app=app)

def test_get_products():
    response = client.get('/products')
    assert response.status_code == status.HTTP_200_OK



def test_create_product():
    data = {
    "name" : "pozzo porro",
    "category" :"cheese", 
    "sku" : "0001",
    "price_original" : 200,
    "discount_percentage" : 0
    }
    response = client.post("/add/",json.dumps(data))
    assert response.status_code == 200 
    assert response.json()["success"] == True
    # assert response.json()["is_active"] == True