import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(z, max_iters):
    c = z
    for n in range(max_iters):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iters


def mandelbrot_set(xmin, xmax, ymin,ymax,width,height,maxiter):
    r1 = np.linspace(xmin,xmax,width)
    r2 = np.linspace(ymin,ymax,height)
    return (r1,r2, [mandelbrot(complex(r,i), maxiter) for r in r1 for i in r2])

x=mandelbrot_set(-2.0, 0.5,-1.25,1.25,1000,1000,80)

y_list = np.array(x[1])
z_list = np.array(x[2])
x_list = np.array(x[0])

N = int(len(z_list)**.5)
z = z_list.reshape(N, N)
plt.imshow(z, extent=(np.amin(x_list), np.amax(x_list), np.amin(y_list), np.amax(y_list)), aspect = 'auto',cmap='prism', interpolation='none')

plt.colorbar()
plt.show()
