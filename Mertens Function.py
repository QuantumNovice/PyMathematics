import matplotlib.pyplot as plt
from numpy import *


def is_square_free(factors):
    for i in factors:
        if factors.count(i) > 1:
            return False
    return True
    

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def mobius_function(n):
    factors = prime_factors(n)
    if is_square_free(factors):
        if len(factors)%2 == 0:
            return 1
        elif len(factors)%2 != 0:
            return -1
    else:
        return 0

def mertens_function(n):
    return sum([mobius_function(i) for i in range(n)])

a = prime_factors(54)
print(a)
print(is_square_free(a))
print('-'*10)
y_range = x_range = 100
x = range(0, x_range)

y = x
z = []
for i in x:
    for j in y:
        z.append( mertens_function(i) + mertens_function(j) )
z = array(z).reshape(x_range, y_range)

#plt.plot(x,y)

plt.contourf(x,y,z, cmap='gnuplot')
plt.show()
