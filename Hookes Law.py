from numpy import *
import matplotlib.pyplot as plt


def law(x, L1, L2,k=1):
    if x <  L1:
        return k*x
    elif x >= L1 and x <= L2:
        return k*exp(x)
    elif x > L2:
        return x**2

x = linspace(0,10,100)
y = [law(i, 2, 5) for i in x]

plt.plot(x,y)
plt.show()
