from objects import *

def norme1(intersection1, intersection2):
    return abs(intersection1[0] - intersection2[0]) + abs(intersection1[1] - intersection2[1])

def initializeVehicleList(grid):
    n = grid.vehicleNumber
    VehicleList = []
    for i in range(n):
        v = Vehicle()
        VehicleList.append(v)

    return VehicleList

#
