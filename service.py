from typing import List
from models import Product, Discount

class DiscountService:
    @staticmethod
    def apply_discounts(products: List[Product], discounts: List[Discount]) -> List[Product]:
        print("products", products)
        print("discounts", discounts)
        for product in products:
            applicable_discounts = [d for d in discounts if (d.sku == product.sku) or (d.category == product.category)]
            if not applicable_discounts:
                continue
            max_discount = max(applicable_discounts, key=lambda x: x.percentage)
            product.discount_percentage = max_discount.percentage
            product.final_price = product.price - (product.price * (max_discount.percentage / 100))


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