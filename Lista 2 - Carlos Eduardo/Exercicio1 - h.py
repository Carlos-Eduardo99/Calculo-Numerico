# -*- coding: utf-8 -*-
"""
Created on Mon Feb 8 14:55:55 2021

@author: Carlos
"""

import numpy as np
import matplotlib.pyplot as plot

print('Exerício 1')
print('h)')
 
def f(x):
    return (np.e**x - x**2 - 10)
def fl(x):
    return (np.e**x - 2*x)
interval = np.linspace(0,4)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()