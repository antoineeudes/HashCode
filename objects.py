from tools import *


class Grid:

    def __init__(self):
        rows = 0
        columns = 0
        vehicleNumber = 0
        rideNumber = 0
        bonus = 0
        timeLimit = 0

class Vehicle:


    def __init__(self):
        self.position=[0,0]
        self.remainingTime=0
        self.virtualPosition=[0,0]
        self.rides = []

    def addRide(self, ride):
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
        index = -1
        startIntersection = [0,0]
        finishIntersection = [0,0]
        travelDuration = 0
        earliestStart = 0
        latestFinish = 0
        startTime=False
        vehicle=False

    def isReachable(self, vehicle):
        #Tell if a vehicle can reach a ride and arrive on time
        return norme1(vehicle.position, self.startIntersection) + vehicle.remainingTime + travelDuration < latestFinish
