# -*- coding: utf-8 -*-
"""
Created on Mon Feb 8 14:48:55 2021

@author: Carlos
"""
import numpy as np
import matplotlib.pyplot as plot

print('Exerício 1')
print('f)')

def f(x):
    return (x**3 + 3*x -1)
def fl(x):
    return (3*x + 3)

interval = np.linspace(0,5)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()

