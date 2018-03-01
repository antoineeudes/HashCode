from copy import deepcopy

def read(fichier):
    document = open(fichier, "r")

    for line in document:
        M=[]
        J = line.strip().split(' ')

        for x in J:

            M.append(int(x))

        L.append(deepcopy(M))

    document.close()
    return L

def listRides(fichier):
    L = read(fichier)
    Rides = []
    n = len(L)
    for i in range(1, n):
        r = Ride()
        r.index = i-1
        r.startIntersection = [L[i][0], L[i][1]]
        r.finishIntersection = [L[i][2], L[i][3]]
        r.earliestStart = L[i][4]
        r.latestFinish = L[i][5]
        r.travelDuration = norme1(r.finishIntersection, r.startIntersection)

        Rides.append(r)
    return Rides

def getGrid():


def write(listVehicles):
    document = open("output.in", "w")
    for vehicle in listVehicles:
        n = len(vehicle.rides)
        document.write(n)
        document.write(" ")

        for i in range(n):
            document.write(vehicle.rides[i].index)
            if i < n-1:
                document.write(" ")

        document.write("\n")
