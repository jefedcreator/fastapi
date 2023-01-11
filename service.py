from typing import List
from models import Product, Discount

class DiscountService:
    @staticmethod
    def apply_discounts(products: List[Product], discounts: List[Discount]) -> List[Product]:
        sku_discounts = {d.sku: d.percentage for d in discounts if d.sku is not None}
        category_discounts = {d.category: d.percentage for d in discounts if d.category is not None}
        max_discount = max([d.percentage for d in discounts])

        for product in products:
            discount = max_discount
            if product.sku in sku_discounts:
                discount = max(discount, sku_discounts[product.sku])
            if product.category in category_discounts:
                discount = max(discount, category_discounts[product.category])
            if discount != max_discount:
                product.discount_percentage = discount
                product.price = product.price - (product.price * discount) / 100
            else:
                product.discount_percentage = None
        return products
