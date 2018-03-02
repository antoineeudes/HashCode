from tools import norme1


class Grid:

    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.vehicleNumber = 0
        self.rideNumber = 0
        self.bonus = 0
        self.timeLimit = 0


class Vehicle:

    def __init__(self):
        self.position=[0,0]
        self.remainingTime=0
        self.virtualPosition=[0,0]
        self.rides = []

    def addRide(ride):
        self.rides.append(ride)
        self.remainingTime=norme1(self.position, ride.startIntersection)+norme1(ride.finishIntersection,ride.startIntersection)
        self.position=ride.finishIntersection

    def refresh():
        if remainingTime==0:
            return None
        else:
            self.remainingTime-1

    def free():
        self.remainingTime = 0


class Ride:

    def __init__(self):
        self.index = -1
        self.startIntersection = [0,0]
        self.finishIntersection = [0,0]
        self.travelDuration = 0
        self.earliestStart = 0
        self.latestFinish = 0
        self.startTime=False
        self.vehicle=False

    def isReachable(vehicle):
        #Tell if a vehicle can reach a ride and arrive on time
        return norme1(vehicle.position, self.startIntersection) + vehicle.remainingTime + travelDuration < latestFinish
