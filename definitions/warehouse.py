from definintions.product import Product
from ..point import Point



class Warehouse:

    def __init__(self, id: int, pos: Point, products):
        self.pos = pos
        self.products = products
        self.id = id

    def is_empty(self):
        return len(self.products) == 0

    def update_product(self, id, quantity, keyword):
        if keyword == 'add':
            self.products[id] += quantity

        else:
            if self.products[id] >= quantity:
                self.products[id] -= quantity
