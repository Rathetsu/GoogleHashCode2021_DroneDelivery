def is_order_complete(order,payload):
    for item in order:
        if item not in payload or payload[item] != order[item]:
            return False

    return True
    
def find_hq(warehouses,orders):
    """
    Finds  the closes warehouse to all orders such that drones cand drop products there

    """
    min_warehouse = None
    min_dist = 1e12
    for warehouse in warehouses:
        total_dist = 0
        for order in orders:
            dist = warehouse['pos'].distance(order.pos)
            total_dist += dist
        
        if total_dist < min_dist:
            min_dist = total_dist
            min_warehouse = warehouse

    return min_warehouse

def get_easiest_order(orders,drones,warehouses):
    """"
    returns the order which takes the least time for a specific drone

    """
    pass


