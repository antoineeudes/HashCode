from objects import *
from reading import *
from tools import *

grid = getGrid("a_example.in")

listRides = listRides("a_example.in")
VehicleList = initializeVehicleList(grid)

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

def action_t(t,vehiclelist,ridelist, grid):
    temps='Etape '+ str(t)

    n = len(ridelist)
    print(temps)        #On tient au courant l'utilisateur de l'etape ou on en est

    for i in range(grid.vehicleNumber):
        v=vehicleList[i]          #Pour chaque vehicule
        if (v.remainingTime==0):    #Si le vehicule est libre
            p=vehicle.position

            objectif=-5000 #valeur arbitraire, on veut maximiser objectif
            ride_obj=ridelist[0]

            for j in range(n):
                r=ridelist[j]           #Pour chaque ride
                if r.isReachable(v):  #si elle est atteignable
                    obj_j=-norme1(p,r.startIntersection)

                    if (norme1(p,r.startIntersection) <= (r.earliestStart - t)):
                        obj_j += bonus
                    if (obj_j>objectif):
                        objectif=obj_j
                        ride_obj=r

            v.addRide(ride_obj)

    return None


def assignmentVehicles(vehiclelist, ridelist, grid):
    for t in range(grid.timeLimit):
        action_t(t, vehiclelist, ridelist, grid)
    write(vehiclelist)

if __name__ == "__main__":
    assignmentVehicles(VehicleList, listRides)
