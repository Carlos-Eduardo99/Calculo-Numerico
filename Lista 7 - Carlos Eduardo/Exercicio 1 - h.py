# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:45:17 2021

@author: Carlos
"""
import numpy as np

def f(x):
    return np.e**x - x**2 - 10

def secante(a, b ,Tol, n):
    x_anterior = float("NaN")
    x = a
    x_anterior = b 
    for k in range(0,n):
        error = abs ((x-x_anterior)/(max(x,1)))
        print(k,x,f(x), error)
        
        if f(x) == 0 or error < Tol:
            break
        xa = x - f(x) * ((x-x_anterior)/ f(x) -f(x_anterior))
        x_anterior = x
        x = xa
    return x

print(f'Raiz aproximada encontrada: {(secante(2.91,2.93, 0.00001, 20)):.5f}') 
