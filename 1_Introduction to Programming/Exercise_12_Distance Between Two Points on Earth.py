import math
from math import sin, cos

RADEARTH = 6371.01 

latt1 = float(input("Enter the Points for Latitude (t1, g2): \nt1 = "))
latg1 = float(input("g1 = "))

longt2 = float(input("Enter the Points for Longitude (t2, g2): \nt2 = "))
longg2 = float(input("g2 = "))

rlatt1 = math.radians(latt1)
rlatg1 = math.radians(latg1)
rlongt2 = math.radians(longt2)
rlongg2 = math.radians(longg2)

dis = RADEARTH * math.acos(sin(rlatt1) * sin(rlongt2) + cos(rlatt1) * cos(rlongt2) * cos(rlatg1 - rlongg2))

print("The Distance Between These Points:", dis)