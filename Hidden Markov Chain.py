from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import random

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

def plot_markov():
    dim = 2
    n = dim
    T = np.random.random((n,n))
    x = np.random.random((n,1))


    X=[]
    for i in range(x.shape[0]):
        X.append([])
        
    for i in range(100):
        #print (x.shape)
        for j in range(x.shape[0]):
            X[j].append(x[j])
        x = np.matmul(T,x)
        #x = T*x
        
        for a in range(T.shape[1]-1):
            b = random.randint(0, T.shape[0]-1)
            T[a][b]= random.random()

        
        #print(T)
    for i in X:
        #Plot properly normalized vectors only
        if max(i) <= 1:
            plt.plot(i)

for i in range(100):
    plot_markov()
plt.show()
