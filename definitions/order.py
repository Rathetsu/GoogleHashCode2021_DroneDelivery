class Order:
    def __init__(self,id,pos,shooping_cart):
        self.items = shooping_cart
        self.pos = pos
        self.id = id

    
    def is_done(self):
        return len(self.items) == 0
