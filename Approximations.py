import matplotlib.pyplot as plt
from numpy import *


x = linspace(0, 10, 100)
y = sin(x)
a = linspace(0, 10,100)
plt.plot(x,y)

for a in range(100):
    L = sin(a)+ (x-a)*cos(a)
    plt.plot(x, L)
plt.show()
