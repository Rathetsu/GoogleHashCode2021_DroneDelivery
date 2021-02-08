from collections import defaultdict


def check_load_and_unload_command(warehouseId, warehousesNumber, productTypeId, productTypesNumber, itemsNumber):
    checks = [
        0 <= warehouseId < warehousesNumber,
        0 <= productTypeId < productTypesNumber,
        itemsNumber > 0
    ]

    return all(checks)


def check_deliver_command(orderId, ordersNumber, productTypeId, productTypesNumber, itemsNumber):
    checks = [
        0 <= orderId < ordersNumber,
        0 <= productTypeId < productTypesNumber,
        itemsNumber > 0
    ]

    return all(checks)


def check_wait_command(turnsToWait, turnsNumber):
    return turnsToWait < turnsToWait < turnsNumber


def check_command(command, dronesNumber, turnsNumber, warehousesNumber, productTypesNumber, ordersNumber):
    elements = list(command.split())
    if not 0 <= int(elements[0]) < dronesNumber:
        return False

    if elements[1] == 'L' or elements[1] == 'U' and len(elements) == 5:
        return check_load_and_unload_command(int(elements[2]), warehousesNumber, int(elements[3]),
                                             productTypesNumber, int(elements[4]))

    elif elements[1] == 'D' and len(elements) == 5:
        return check_deliver_command(int(elements[2]), ordersNumber, int(elements[3]),
                                     productTypesNumber, int(elements[4]))

    elif elements[1] == 'W' and len(elements) == 3:
        return check_wait_command(int(elements[2]), turnsNumber)

    else:
        return False


def validate_output_file(filename, dronesNumber, turnsNumber, warehousesNumber, productTypesNumber, ordersNumber):
    dronesTurns = defaultdict(lambda: 0)

    with open(filename, 'rt') as file:
        Q = int(file.readline())
        if not 0 <= Q < dronesNumber * turnsNumber:
            return False

        for command in file:
            dronesTurns[command[0]] += 1
            check = check_command(command, dronesNumber, turnsNumber,
                                  warehousesNumber, productTypesNumber, ordersNumber)
            if not check:
                raise Exception('Command Error:' + command)

    check = all(eachDroneTurns < turnsNumber for eachDroneTurns in dronesTurns.values())
    if not check:
        raise Exception('Error: Drone exceeds maximum number of turns')

    print('Succeeded!')


validate_output_file('example.txt', 3, 50, 2, 3, 3)
