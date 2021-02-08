from parse import parse_file
from definitions.drone import Drone
from definitions.point import Point

input_path = 'busy_day.in'
state = parse_file(input_path)
n_drones = state['num_drones']
T = state['deadline']
weights = state['weights']
max_payload = state['max_payload']
warehouses = state['warehouses_list']
orders = state['orders_list']
drones = []
for i in range(n_drones):
    drones.append(Drone(i,max_payload,Point(warehouses[0].pos)))

for t in range(T):
    pass

