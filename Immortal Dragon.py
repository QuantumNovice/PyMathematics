import matplotlib.pyplot as plt
from numpy import *
from sympy import *
'''
An immortal dragon guards a village. Every year, the villagers give this dragon a sack with two pounds of gold coins in exchange for protection, and every year, upon receiving this gold, the dragon puts all her gold together, takes the reciprocal of what she has, keeps it, and spends the rest on food and other things. This yearly cycle goes on for a very long time. How much gold will the dragon ultimately end up with?'''
y = []
dragon = 0
for year in range(1,100):
    dragon += 2
    #if dragon!=0:
         #dragon = Rational(1,dragon)
    dragon = 1/dragon
    #print(dragon)
    
    y.append(dragon)

print(y[-1] == sqrt(2)-1)

##for i in range(len(y)):
##    print(i+1, y[i])


