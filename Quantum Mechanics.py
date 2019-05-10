import matplotlib.pyplot as plt
from numpy import *


class InfiniteSquareWell:
    def __init__(self):
        self.L = 1
        self.k = 1
        self.h =1
        self.h_bar = 1/(2*pi)
        self.m = 1
        self.x_c = 0
        self.infinity = 100*self.x_c+1
        self.A = 1
        
    def PE(self,x):
        print(x)
        if (x < self.x_c + self.L/2) and (x > self.x_c - self.L/2):
            return 0
        else:
            return self.infinity

    def k_n(self,n):
        return (n*pi)/self.L

    def energy(self,n):
        return (n**2 * pi**2 * self.h_bar**2)/(2*self.m*self.L**2)

    def psi(self,n, x, t):
        omega_n = self.energy(n)/self.h_bar
        return self.A*sin(self.k_n(n)*(x-self.x_c + (self.L/2)))*exp(-1j*omega_n*t)
    
    def position(self,n,x):
        if (x < self.x_c + self.L/2) and (x > self.x_c - self.L/2):
            return (2/self.L)*( sin(self.k_n(n)*(x-self.x_c + (self.L/2))) )**2
        else:
            return 0
        
w = InfiniteSquareWell()

x = linspace(-2,2,100)
y = []
for i in x:
    y.append(w.psi(1,i,1))
    #y.append(w.position(2,i))

##plt.plot(real(y))
##plt.plot(imag(y))
##
##plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
line, = plt.plot(x,real(y))
line2, = plt.plot(x, imag(y))
ax.set_ylim(-2, 2)

i = 0
def update(data):
    global i
    i += 0.1
    data = []
    for j in x:
        data.append( w.psi(1,j,i))
        
    line.set_ydata(real(data))
    line2.set_ydata(imag(data))
    return line,



ani = animation.FuncAnimation(fig, update, interval=100)
plt.show()
