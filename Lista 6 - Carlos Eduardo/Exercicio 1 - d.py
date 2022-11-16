# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:32:40 2021

@author: Carlos
"""

def f(x):
    return x**2 + 2*x + 1

def f1(x):
    return (2*x+2)


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

print(f'A raiz aproximada é: {NewtonRaphson(-2, 0, 0.00001, 20):.5f}')