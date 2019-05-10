import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1,1000)
y = np.linspace(1,-1, 1000)

plt.plot(x,y)
plt.plot(x,-y)
plt.plot(2*x,2*y)

plt.show()
