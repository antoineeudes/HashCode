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
    L = read(fichier)
    g = Grid()
    g.rows = L[0][0]
    g.columns = L[0][1]
    g.vehicleNumber = L[0][2]
    g.rideNumber = L[0][3]
    g.bonus = L[0][4]
    g.timeLimit = L[0][5]
    return g


def write(listVehicles):
    document = open("output.in", "w")
    for vehicle in listVehicles:
        n = len(vehicle.rides)
        document.write(str(n))
        document.write(" ")

        for i in range(n):
            document.write(str(vehicle.rides[i].index))
            if i < n-1:
                document.write(" ")

        document.write("\n")
