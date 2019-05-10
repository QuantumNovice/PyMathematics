import matplotlib.pyplot as plt
from math import *
import numpy as np
import random

def p(formula):
    y = []
    for x in np.arange(-2*np.pi, 2*np.pi, 0.1):
       y.append(eval(formula))
    return y

for i in np.arange(-2,2,0.1):
    plt.plot(p('sec(x)+i'))
             
plt.show()
