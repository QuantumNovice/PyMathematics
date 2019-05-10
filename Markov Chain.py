from sympy import *
import matplotlib.pyplot as plt
import numpy as np

T = Matrix([
    [-0.6, -0.4, -0.6,],
    [-0.1, -0.1, -0.2],
    [-0.3, -0.5, -0.2]
    ])

x = Matrix([
    [0.5],
    [0.5],
    [-0.5]
    ])

dim = 2
n = dim
T = np.random.random((n,n))*-1
x = np.random.random((n,1))


X=[]
for i in range(x.shape[0]):
    X.append([])
    
for i in range(20):
    #print (x.shape)
    for j in range(x.shape[0]):
        X[j].append(x[j])
    x = np.matmul(T,x)
    #x = T*x
for i in X:
    plt.plot(i)
plt.show()
