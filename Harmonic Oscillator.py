'''
Author: Novice
14-2-2019
'''

from numpy import *
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self):
        self.mass = 1
        self.k = 1
        self.angular_frequency = sqrt(self.k/self.mass)
        self.A = 6
        self.E = 0.5*self.k*self.A**2

    def force(self,x):
        return -self.k*x

    def position(self, t, A, phase):
        return A*cos(self.angular_frequency*t + phase)

    def kinetic_energy(self, x):
        return (0.5*self.mass*self.angular_frequency**2)*(self.A**2-x**2)

    def potential_energy(self, x):
        return self.E - self.kinetic_energy(x)

    def hamiltonian(self,x):
        return self.potential_energy(x)+self.kinetic_energy(x)

    def lagrangian(self,x):
        return self.kinetic_energy(x)-self.potential_energy(x)
    
    
o = HarmonicOscillator()
x = linspace(-6,6,100)


plt.subplot(2,2,1)
plt.plot(o.force(x), o.potential_energy(x))
plt.xlabel('Applied Force')
plt.ylabel('Potential')

plt.subplot(2,2,2)
plt.plot(o.force(x),o.position(x,1,1))
plt.xlabel('Applied Force')
plt.ylabel('Position')


plt.subplot(2,2,3)
plt.plot(o.potential_energy(x), label='Potential Energy')
plt.plot(o.kinetic_energy(x), label='Kinetic Energy')
plt.xlabel('Displacement')
plt.ylabel('Energy')
plt.legend()

plt.subplot(2,2,4)
plt.plot(o.hamiltonian(x), label='Hamiltonian')
plt.plot(o.lagrangian(x), label='Lagrangian')
plt.xlabel('Displacement')
plt.ylabel('Energy')
plt.legend()
plt.show()  
