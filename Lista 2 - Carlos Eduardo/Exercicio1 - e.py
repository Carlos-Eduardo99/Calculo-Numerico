# -*- coding: utf-8 -*-
"""
Created on Sun Feb 7 14:39:34 2021

@author: Carlos
"""
from math import e
import numpy as np
import matplotlib.pyplot as plot

print('Exerício 1')
print('e)') 

def f(x):
    return (np.e**(2-(x**2))*(x+1)**2)
def fl(x):
    return ((e**(2-x**2))*(-2*x)) * ((x+1)**2) + e**(2-x**2) * (2*(x+1))

interval = np.linspace(-1.6, -1)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()