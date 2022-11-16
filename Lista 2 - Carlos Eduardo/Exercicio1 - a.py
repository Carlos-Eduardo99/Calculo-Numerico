# -*- coding: utf-8 -*-
"""
Created on Sun Feb 7 14:15:54 2021

@author: Carlos
"""
import numpy as np
import matplotlib.pyplot as plot

print('Exerício 1')
print('a)') 

def f(x):
    return (np.log(x))
def fl(x):
    return (1/x)
interval = np.linspace(1,5)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()

