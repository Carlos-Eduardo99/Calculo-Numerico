# -*- coding: utf-8 -*-
"""
Created on Sun Feb 7 14:30:47 2021

@author: Carlos
"""

import numpy as np
import matplotlib.pyplot as plot

print('Exerício 1')
print('b)') 

def f(x):
    return (np.e**x)
def fl(x):
    return (np.e**x)

interval = np.linspace(0.5, 1.5)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()