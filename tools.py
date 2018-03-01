from objects import Vehicle

def norme1(intersection1, intersection2):
    return abs(intersection1[0] - intersection2[0]) + abs(intesection1[1] - intersection2[1])

def initializeVehicleList(grid):
    n = grid.vehicleNumber
     VehicleList = []
     for i in range(n):
         v = Vehicle()
         VehicleList.append(v)

    return VehicleList

def virtualDistance(ride, vehicle, time, maxTime):
    dist =
    if time >= ride.latestFinish - ride.travelDuration - norme1(ride.startIntersection, vehicle.position) - :
        #Cannot be achieved in time
        return maxTime
    else:

    s = vehicle.remainingTime + norme1(ride.startIntersection, vehicle.position) - 
