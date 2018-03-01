from objects import *
from reading import *

r = Ride()
r.index = 0



v = Vehicle()
v.addRide(r)

listVehicles = [v]

write(listVehicles)
