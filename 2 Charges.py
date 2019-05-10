import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from numpy import *

def E(x,y,k=1,Q=1,scale=1):
    return scale*((k*Q)/(x**2+y**2))

def V(x,y,k=1,Q=1,scale=1):
    return scale*((k*Q)/sqrt(x**2+y**2))

x = linspace(-10,10,100)
y = x



plt.subplot(1,2,1)
z = E(xx,yy)+E(xx+5,yy+5)
plt.title('Electric Field of 2 charges')
plt.contourf(xx,yy,z, levels=linspace(0,1,200))


plt.subplot(1,2,2)
z = V(xx,yy)+V(xx+5,yy+5)
plt.title('Equi-potential of 2 charges')
plt.contourf(xx,yy,z, levels=linspace(0,1,200))
plt.show()
