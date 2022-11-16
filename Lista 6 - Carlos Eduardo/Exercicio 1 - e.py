# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:52:35 2021

@author: Carlos
"""
from math import e
import numpy as np


def f(x):
    return np.e**(2-(x**2))*(x+1)**2


def f1(x):
    return ((e**(2-x**2))*(-2*x)) * ((x+1)**2) + e**(2-x**2) * (2*(x+1))

def NewtonRaphson(a, b, Tol, n):
    xAnt = float("Nan")
    x = a
    for k in range(0, n):
        erro = abs((x - xAnt)/(max(x, 1)))
        print(f'Iteração: {k}, x: {x:.5f}, f(x): {f(x):.5f}, erro: {erro:.5f}')
        if f(x) == 0 or erro < Tol:
            break
        xAnt = x
        x = x - (f(x)/f1(x))
    return x

print(f'A raiz aproximada é: {NewtonRaphson(-2, -0.5, 0.00001, 20):.5f}')
print("Raiz indefinida")