from typing import List
from models import Product, Discount

class ProductService:
    @staticmethod
    def apply_discounts(products: List[Product], discounts: List[Discount]) -> List[Product]:
        print("products", products)
        print("discounts", discounts)
        for product in products:
            applicable_discounts = [d for d in discounts if (d.sku == product.sku) or (d.category == product.category)]
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
        return [product for product in products if product["category"] == query]

    def filter_products_by_price(products : List[Product], query: int) -> List[Product]:
        return [product for product in products if int(product["price"]) <= query]

    def filter_products_by_price_category(products : List[Product], price_query: int, query : str) -> List[Product]:
        return [product for product in products if int(product["price"]) <= price_query and product["category"] == query]

