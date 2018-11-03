'''
transformation.py
python3.6
Author: Novice
Plot Transformation Vectors
'''
import matplotlib.pyplot as plt
#from sympy import *

import math#, random
from numpy import *

# Some Transformations
# Reflection, Projection, Rotation, Shear
Rx = [
    [1, 0],
    [0, -1]
    ]

Ry = [
    [-1, 0],
    [0, 1]
    ]

Ryx = [
    [0, 1],
    [1, 0]
    ]

Rxy = [
    [0, -1],
    [-1, 0]
    ]

Px = [
    [1, 0],
    [0, 0]
    ]

Py = [
    [0, 0],
    [0, 1]
    ]

def rotation(degree):
    degree= math.radians(degree)
    return [
        [cos(degree), -sin(degree)],
        [sin(degree), cos(degree)]
        ]

def Shearx(k):
    return [
        [1, k],
        [0, 1]
        ]

def Sheary(k):
    return [
        [1, 0],
        [k, 1]
        ]

def toTuple(matrix):
    ''' Convert Matrix --> Tuple'''
    return [0,matrix[0][0]], [0,matrix[1][0]]

def transform(A, u):
    ''' Plots position vector before and after transformation'''
    z = toTuple(u)
    plt.plot(z[0], z[1], 'g-') # Make Initial Vectors Green
    
    T = toTuple(matmul(A,u))
    plt.plot(T[0], T[1], 'b-') # Make transformed vector blue

def fig_transform(A,U):
    ''' Plots position vectors before and after transformation'''
    for u in U:
        transform(A,u)

if __name__ == '__main__':
    u1 = [
            [0],
            [0]
            ]
    u2 = [
            [1],
            [0]
            ]
    u3 = [
            [0],
            [1]
            ]
    U = [u1,u2,u3]
    #U = [ [[random.randint(-5,5)], [random.randint(-5,5)]] for i in range(100)]

    fig_transform(rotation(45),U)
    plt.show()
