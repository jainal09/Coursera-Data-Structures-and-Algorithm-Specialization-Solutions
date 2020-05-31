import sys


def petrol(tank_fuel, tank_capacity, i, stops_array, num_refill, total_distance):
    if i + 1 < len(stops_array):
        to_travel = stops_array[i + 1] - stops_array[i]
        to_travel_check = tank_fuel - to_travel

        if to_travel_check < 0:
            num_refill = num_refill + 1
            tank = tank_capacity - to_travel
            if tank < 0:
                status = {
                    "journey": False,
                    "fill": True,
                    "num_refill": num_refill,
                    "tank": tank
                }
                return status

            else:
                status = {
                    "journey": True,
                    "fill": True,
                    "num_refill": num_refill,
                    "tank": tank
                }
                return status

        else:
            tank = tank_fuel - to_travel
            status = {
                "journey": True,
                "fill": False,
                "tank": tank,
                "num_refill": num_refill,
            }
            return status

    else:
        to_travel = total_distance - stops_array[i]
        to_travel_check = tank_fuel - to_travel

        if to_travel_check < 0:
            tank = tank_capacity
            enough_fuel = tank - to_travel

            if enough_fuel < 0:
                status = {
                    "journey": False,
                    "fill": True,
                    "num_refill": num_refill,
                    "tank": tank
                }
                return status

            else:
                num_refill = num_refill + 1
                status = {
                    "journey": True,
                    "fill": True,
                    "num_refill": num_refill,
                    "tank": tank
                }

                return status

        else:
            tank = tank_fuel - to_travel
            status = {
                "journey": True,
                "fill": False,
                "tank": tank
            }
            return status


def compute_min_refills(distance, tank, stops):
    tank_capacity = tank
    num_refill = 0
    cant_travel = False
    stops.insert(0, 0)
    for i in range(len(stops)):
        status = petrol(tank_fuel=tank, tank_capacity=tank_capacity, i=i, stops_array=stops, num_refill=num_refill,
                        total_distance=distance)
        if status["journey"] and not status["fill"]:
            tank = status["tank"]
        elif not status["journey"]:
            cant_travel = True
            break
        else:
            num_refill = status["num_refill"]
            tank = status["tank"]
    if cant_travel:
        return -1
    else:
        return num_refill


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = [int(x) for x in sys.stdin.readline().split()]
    if len(stops) < n:
        for i in range(n-1):
            x = int(input())
            stops.append(x)

    print(compute_min_refills(d, m, stops))
