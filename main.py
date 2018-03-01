from objects import *
from reading import *
from tools import *

grid = getGrid("a_example.in")

listRides = listRides("a_example.in")
VehicleList = initializeVehicleList(grid)


r = Ride();
r.index = 10

v = Vehicle()
v2 = Vehicle()

# for ride in listRides:
#     v.addRide(ride)

n=len(listRides)
for i in range(int(n/2)):
    v.addRide(listRides[i])


for i in range(1, n):
    v2.addRide(listRides[i])

# v2.addRide(r)

# print(len(v2.rides))

listVehicles = [v, v2]

write(listVehicles)
