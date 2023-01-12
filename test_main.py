from main import app
import json
from fastapi import FastAPI
from starlette.testclient import TestClient

client = TestClient(app)

def test_add_products():
    data = {
        "category" : "coffee",
        "sku" : "003",
        "name" : "cappuchino",
        "price" : 300
    }
    response = client.post("/discounts/",json=data)
    assert response.status_code == 200 
    assert response.json()["success"] == True

def test_add_discount():
    data = {
        "category" : "coffee",
        "percentage" : 15
    }
    response = client.post("/discounts/",json=data)
    assert response.status_code == 200 
    assert response.json()["success"] == True


def test_get_products():
    response = client.get('/products')
    assert response.status_code == 200