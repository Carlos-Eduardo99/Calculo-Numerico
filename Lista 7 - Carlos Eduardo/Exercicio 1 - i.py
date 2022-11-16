# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:46:46 2021

@author: Carlos
"""
import numpy as np

def f(x):
    return -np.cos(x) + np.sqrt(x)

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

print(f'Raiz aproximada encontrada: {(secante(0,2, 0.00001, 20)):.5f}')