#######################
# ASTRONOMY FUNCTIONS #
#######################

import math

def deg2rad(angle):
   """
   Function that converts angle from degrees to radians.
   """
   rad_angle = angle * math.pi / 180.0
   return rad_angle

def rad2deg(angle):
   """
   Function that converts angle from radians to degrees.
   """
   deg_angle = angle * 180.0 / math.pi 
   return deg_angle

def projected_distance(ra1, ra2, dec1, dec2):
   """
   Function that returns the projected distance (in arcminutes) between two points.
   """
   if ra1 == ra2 and dec1 == dec2:
      return 0.0
   else:
      dist = math.acos(math.sin(deg2rad(dec1)) * math.sin(deg2rad(dec2)) + math.cos(deg2rad(dec1)) * math.cos(deg2rad(dec2))
                    * math.cos(deg2rad(ra1) - deg2rad(ra2)))
      return rad2deg(dist) * 60
