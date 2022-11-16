# -*- coding: utf-8 -*-
"""
Created on Mon Feb 8 15:04:46 2021

@author: Carlos
"""
import numpy as np
import matplotlib.pyplot as plot

print('Exerício 1')
print('j)') 

def f(x):
    return (x-3-(x**-x))
def fl(x):
    return - x**(-x) * np.log(x) * (-1)
interval = np.linspace(0,5)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()
