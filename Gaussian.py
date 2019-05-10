import matplotlib.pyplot as plt
from numpy import *

def gaussian(x, mu=0,sigma=1):
    return (1/sqrt(2*pi*sigma**2))*exp(-((x-mu)**2)/(2*sigma**2))

def gaussian2d(x,y,mu=0, sigma=1):
    return gaussian(x,mu=mu,sigma=sigma)*gaussian(y,mu=mu,sigma=sigma)

x = linspace(-3, 3, 300)
y = linspace(-3,3,300)
xx,yy = meshgrid(x,y)
z = (gaussian2d(xx,yy)+gaussian2d(1/xx,1/yy))**3
#plt.contourf(x,y,z)
plt.pcolor(x,y,z,cmap='gnuplot')
plt.show()

