from sympy import *
from math import degrees, radians
import numpy as np



def toCartesian(matrix):
    '''Converts mixed system input to Cartesian'''
    if matrix.dtype != '<U11':
        return matrix
    new_matrix = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            #print(matrix[i][j])
            reader = matrix[i][j]
            if reader.startswith('@'):
                #print('Angle')
                angle = radians(int(reader.replace('@', '')))
                matrix[i][j] = int(matrix[i][j-1])*sin(angle)
                matrix[i][j-1] = int(matrix[i][j-1])*cos(angle)
    return np.array(matrix,dtype=float)

def cross(m1,m2):
    # Cross Product of M1 and M2
    matrix = np.zeros((m1.shape[0],1))
    for i in range(m1.shape[0]):
        for j in range(m1.shape[1]):
            #print(m1[i][j],m2[i][j])
            try:
                matrix[i] = m1[i][j]*m2[i][j+1] - m1[i][j+1]*m2[i][j]
            except:
                pass
    return matrix

#________________________________________________________

#Theta_x
forces = np.array(
    [
    [4,'@15'],
    [0,2]
    [-3.5,0]
    ])
moment_arms = np.array(
    [
    [10,40],
    [80,0]
    ])

moments = np.array([-300,300])

''' Sum all moments'''
m= 0
for i in range(moments.shape[0]):
    m += moments[i]
moments = m

forces = toCartesian(forces)
moment_arms = toCartesian(moment_arms)

moment = cross(moment_arms,forces)
moments = sum(moment)+moments

print(sum(forces),'\n', moment_arms,'\n', moments)
