from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')

def S(x):
    return 3*sqrt(2)*sqrt(pi)*fresnels(sqrt(2)*x/sqrt(pi))*gamma(3/4)/(8*gamma(7/4))

def C(x):
    return sqrt(2)*sqrt(pi)*fresnelc(sqrt(2)*x/sqrt(pi))*gamma(1/4)/(8*gamma(5/4))

y_range = x_range = 100
x = np.linspace(-5,5,x_range)
y = x
z = []

for i in x:
    for j in y:
        z.append(S(i)+C(j))

z = np.array(z).reshape(x_range, y_range)
plt.contourf(x,y,z)
plt.show()
