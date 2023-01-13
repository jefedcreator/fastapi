from typing import List
from models import Product, Discount

class ProductService:
    @staticmethod
    def apply_discounts(products: List[Product], discounts: List[Discount]) -> List[Product]:
        print("products", products)
        print("discounts", discounts)
        for product in products:
            applicable_discounts = [d for d in discounts if (d.sku == product.sku) or (d.category == product.category)]
            print("applicable_discounts", applicable_discounts)
            if applicable_discounts:
                max_discount = max(applicable_discounts, key=lambda x: x.percentage)
                product.price = {
                    "original": product.price,
                    "final": product.price - (product.price * (max_discount.percentage / 100)),
                    "discount_percentage": str(max_discount.percentage) + "%",
                    "currency": "USD"
                }
            else:
                product.price = {
                    "original": product.price,
                    "final": product.price,
                    "discount_percentage": None,
                    "currency": "USD"
                }
        return products

    def filter_products_by_category(products : List[Product], query: str) -> List[Product]:
        filtered_product = []
        for product in products:
            if(product["category"] == query):
                filtered_product.append(product)
        return filtered_product

    def filter_products_by_price(products : List[Product], query: int) -> List[Product]:
        filtered_product = []
        for product in products:
            if(int(product["price"]) <= query):
                filtered_product.append(product)
        return filtered_product

    def filter_products_by_price_category(products : List[Product], price_query: int, query : str) -> List[Product]:
        filtered_product = []
        for product in products:
            if(int(product["price"]) <= price_query and product["category"] == query):
                filtered_product.append(product)
        return filtered_product
