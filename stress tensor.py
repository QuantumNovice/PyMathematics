from numpy import *

sigma = 2400*10**6
tau = 75*10**9

sigma_11 = sigma_22 = sigma_33 = sigma
tau_12 = tau_13 = tau_21 = tau_23 = tau_31 = tau_32 = tau

stress_tensor = array([
    [sigma_11, tau_12, tau_13],
    [tau_21, sigma_22, tau_23],
    [tau_31, tau_32, sigma_33],
    ])

area = array([
    [1],
    [1],
    [1]
    ])

ans = matmul(stress_tensor, area )

import matplotlib.pyplot as plt
from numpy import *
x = linspace(-10,10,100)
y = x
xx, yy = meshgrid(x,y)
z = floor(xx)**2
plt.contourf(x,y,z)
plt.show()
