# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 14:37:16 2021

@author: Carlos
"""
import numpy as np
import matplotlib.pyplot as plot

print('Exerício 1')
print('d)') 

def f(x):
    return (x**2 + 2*x + 1)
def fl(x):
    return (2*x+2)

interval = np.linspace(0,5)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()