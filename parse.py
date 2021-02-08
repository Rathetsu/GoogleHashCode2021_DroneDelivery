from definitions.point import Point
from definitions.order import Order
from definitions.warehouse import Warehouse

def parse_file(input_path):

    with open(input_path) as f:

        # parameters of the simulation
        num_rows, num_cols, num_drones, deadline, max_payload = map(
            int, f.readline().split(' '))

        # weights of the products available for orders
        num_products = int(f.readline())
        weights = list(map(int, f.readline().split(' ')))
        assert num_products == len(weights)

        # warehouses and availability of individual product types
        num_warehouses = int(f.readline())
        warehouse_list = []
        for i in range(num_warehouses):
            r, c = map(int, f.readline().split(' '))
            position = Point(r, c)
            warehouse_stock = list(map(int, f.readline().split(' ')))
            assert num_products == len(warehouse_stock)
            warehouse = Warehouse(i,position,warehouse_stock)
            warehouse_list.append(warehouse)

        # customer orders
        num_orders = int(f.readline())
        order_list = []
        for i in range(num_orders):
            r, c = map(int, f.readline().split(' '))
            position = Point(r, c)
            num_products_in_order = int(f.readline())
            product_types_in_order = list(map(int, f.readline().split(' ')))
            assert num_products_in_order == len(product_types_in_order)
            shopping_cart = [0 for i in range(num_products)]
            for product_id in product_types_in_order:
                shopping_cart[product_id] += 1


            order = Order(i,position,shopping_cart)
            order_list.append(order)

    input_data = {
        'num_rows': num_rows,
        'num_cols': num_cols,
        'num_drones': num_drones,
        'deadline': deadline,
        'max_payload': max_payload,
        'weights': weights,
        'warehouse_list': warehouse_list,
        'order_list': order_list,
    }

    return input_data
