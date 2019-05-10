"""
Using the slider widget to control visual properties of your plot.

Author: N0vice
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


def E(x,y,k=1,Q=1,scale=1):
    return scale*((k*Q)/(x**2+y**2))

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

x = np.linspace(-10,10, 100)
y = x
xx, yy = np.meshgrid(x,x)

a0 = 2
f0 = 1
delta_f = 5.0

z = E(xx,yy) + E(xx+a0,yy+f0)

p1 = plt.subplot(111)
p1.contourf(xx, yy, z,levels=np.linspace(0,1,200), cmap='gnuplot')
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'y', 0.1, 10.0, valinit=f0)
samp = Slider(axamp, 'x', 0.1, 10.0, valinit=a0)


def update(val):
    amp = samp.val
    freq = sfreq.val
    p1.cla()
    
    z = E(xx,yy) + E(xx+amp,yy+freq)
    p1.contourf(xx, yy, z,levels=np.linspace(0,1,200))

    fig.canvas.draw_idle()

sfreq.on_changed(update)
samp.on_changed(update)

plt.show()
