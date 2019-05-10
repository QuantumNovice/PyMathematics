from numpy import *
import matplotlib.pyplot as plt

class Charge:
    def __init__(self):
        self.value = 1 # Coulomb
        self.k = 1
        self.position = (0,0)
        self.x_o = self.position[0]
        self.y_o = self.position[1]

    def potential(self, x,y):
        r = sqrt((x+self.x_o)**2 + (y+self.y_o)**2)
        return (self.k*self.value)/r

    def field(self, x,y):
        r = sqrt((x+self.x_o)**2 + (y+self.y_o)**2)
        return (self.k*self.value)/r**2


q = Charge()
x = linspace(-1,1,100)
y = x
xx, yy = meshgrid(x,y)

plt.contour(x,y,q.field(xx,yy), levels=linspace(0,200,500))
plt.show()
