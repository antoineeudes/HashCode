from tools import *


class Grid:
    rows
    columns
    vehicleNumber
    rideNumber
    bonus
    timeLimit

class Vehicle:
    position=[0,0]
    remainingTime=0
    virtualPosition
    rides = []

    def addRide(self, ride):
        rides.append(ride)
        self.remainingTime=norme1(self.position, startIntersection)+norme1(finishIntersection,startIntersection)
        self.position=ride.finishIntersection

    def refresh():
        if remainingTime==0:
            return None
        else:
            self.remainingTime-1

    def free():
        self.remainingTime = 0
        




class Ride:
    startIntersection
    finishIntersection
    earliestStart
    latestFinish
    startTime=False

    vehicle=False

    def isReachable(self, vehicle):
        if norme1(vehicle.position, self.startIntersection) + vehicle.remainingTime <
