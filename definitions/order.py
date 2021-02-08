from point import Point
import sys
sys.path.append('../')


class Order:
    def __init__(self, id: int, pos: Point, shopping_cart):
        self.items = shopping_cart
        self.pos = pos
        self.id = id

    def is_done(self):
        return len(self.items) == 0
