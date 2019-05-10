# Markov Process / Markov Chains in Numpy
import numpy as numpy

# Also called Transition matrix
stochaistic_matrix = np.array(
    [  #Food,Shock
        [0.8, 0.3],# Door_A
        [0.2, 0.7] # Door_B
    ])

probability_matrix = np.array(
    [
        [0.5], # Probability of going through Door_A at Day 0
        [0.5] # Probability of going through Door_B at Day 0
    ])

X_zero = np.matmul(stochaistic_matrix, probability_matrix)
print("X_0",X_zero)
X_one = np.matmul(stochaistic_matrix, probability_matrix)
print("X_1"X_one)