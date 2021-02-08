class Product:
    def __init__(self, id: int, weight):
        self.id = id
        self.weight = weight

    def weight(self):
        return self.weight

    def check_availability(self, warehouses):
        availability = {}
        for warehouse in warehouses:
            if self.id in warehouse.products:
                availability[warehouse.id] += warehouse.products[self.id]

        return availability
