import matplotlib.pyplot as plt
from math import *
import numpy as np
from sympy import *
from sympy.solvers.solveset import linsolve
from random import randint

x,y,z,a,b,c = symbols('x,y,z,a,b,c')
points = [(1,2,), (2,2), (4,5)]

def onParabola(points):
    '''
    y = a*x**2 + b*x + c 
    '''
    quadratic_eq = a*x**2 + b*x + c - y

    linear_equations = []
    for (i,j) in points:
        linear_equations.append( quadratic_eq.subs({x:i, y:j}) )

    try:
        ak, bk, ck = list(linsolve(linear_equations, (a,b,c)))[0]
    except IndexError:
        print('[!] Solution doesn\'t exist')
        return {()}
    return quadratic_eq.subs({a:ak, b:bk, c:ck, y:0})

eq = onParabola(points)
if len(str(eq)) > 1:
    u = np.linspace(-10,10,100)
    v = [eq.subs({x:i}) for i in u]
    plt.plot(u,v, label='Solution Curve')
    for i in points:
        plt.plot(i[0], i[1], 'bo', label='Points')

    plt.legend()
    plt.show()
