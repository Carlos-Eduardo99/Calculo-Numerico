# -*- coding: utf-8 -*-
"""
Created on Mon Feb 8 14:52:26 2021

@author: Carlos
"""
import numpy as np
import matplotlib.pyplot as plot

print('Exerício 1')
print('g)')

def f(x):
    return (np.sin(x) + (x**2) )
def fl(x):
    return (np.cos(x) + 2*x)
interval = np.linspace(-4,5)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()
