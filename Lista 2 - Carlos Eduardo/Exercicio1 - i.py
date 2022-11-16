# -*- coding: utf-8 -*-
"""
Created on Mon Feb 8 14:59:45 2021

@author: Carlos
"""
import numpy as np
import matplotlib.pyplot as plot

print('Exerício 1')
print('i)')
 
def f(x):
    return (-np.cos(x) + np.sqrt(x))
def fl(x):
    return (np.sin(x) + (1/2*np.sqrt(x)))
interval = np.linspace(0,5)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()
