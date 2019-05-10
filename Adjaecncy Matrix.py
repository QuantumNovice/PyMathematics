import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def random_adjacency(n):
    x = np.zeros((n,n))
    for i in range(2*n):
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        x[i][j] = random.randint(0,1)
    return x

T = np.array([
    [0,1,1],
    [0,0,0],
    [1,1,0]
    ])

#T = random_adjacency(10)

for i in range(10):
    T = np.matmul(T,T)
    print(T, i)
    

G = nx.Graph(T)
nx.adjacency_matrix(G)
nx.draw_networkx(G, with_labels=True)
plt.show()


