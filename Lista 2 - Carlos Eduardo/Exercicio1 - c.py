# -*- coding: utf-8 -*-
"""
Created on Sun Feb 7 14:33:40 2021

@author: Carlos
"""
import numpy as np
import matplotlib.pyplot as plot

print('Exerício 1')
print('c)') 

def f(x):
    return (np.cos(x))
def fl(x):
    return (-np.sin(x))
interval = np.linspace(0.5,3)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()


