import matplotlib.pyplot as plt
from math import *
import numpy as np
from sympy import *
from sympy.solvers.solveset import linsolve

def matrixToEq(system):
    variables = 'xyzwt'
    equations = []
    row, col = system.shape
    for i in range(row):
        equation = ''
        for j in range(col):
            #print(system[i, j])
            if j != col-1:
                equation += str(system[i,j])+'*'+variables[j]+' + '
            else:
                equation += str(-1*system[i,j])
            
        equations.append(equation)
    return equations

x,y,z,w,b,c = symbols('x,y,z,w,b,c')

system = Matrix([
    [1,1,3,2,-1],
    [2,-1, 0,1,-5],
    [0,3,6,0,8]
    ])

solution = linsolve(system, (x,y,z,w,b))
q,e,r,t = list(solution)[0]
print( solution )

equations = [sympify(i) for i in matrixToEq(system)]
for i in equations:
    print(i.subs({x:q, y:e, z:r, w:t}))
