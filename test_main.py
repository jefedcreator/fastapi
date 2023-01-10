from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app=app)

def test_home_endpoint():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "hello world"}

def test_get_products_by_category_endpoint():
    response = client.get('/all/coffee')
    assert response.status_code == status.HTTP_200_OK
    # assert response.json() == {"message": "hello world"}

def test_get_products_by_price_endpoint():
    response = client.get('/all/1000')
    assert response.status_code == status.HTTP_200_OK
    # assert response.json() == {"message": "hello world"}