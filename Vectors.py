import math
from math import degrees,radians

def cartesian(r, alpha):
    return r*math.cos(radians(alpha)), r*math.sin(radians(alpha))

def mod(cartesian_tuple):
    return math.sqrt(cartesian_tuple[0]**2 + cartesian_tuple[1]**2)

# Law of Cosine
def lcoss(x,y, alpha):
    return math.sqrt(x**2 + y**2 - 2*x*y*math.cos(radians(alpha)) )

# Law of Sine
def lsinea(a,alpha,b):
    return degrees(math.asin( (math.sin(radians(alpha)) / a) * b))

                     
F = cartesian(200, 51.84)
r = cartesian(20,75)

print(mod(F), mod(r))
print(lcoss(10,20,105))
print(lsinea(24.57, 105,20))


