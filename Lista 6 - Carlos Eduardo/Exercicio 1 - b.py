# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:10:41 2021

@author: Carlos
"""
import numpy as np


def f(x):
    return np.e**x


def f1(x):
    return (np.e**x)


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


print(f'A raiz aproximada é: {NewtonRaphson(0, 5, 0.00001, 20):.5f}')
print("Analisando o gráfico desta função através dos exercícios anteriores, podemos constatar que a mesma não possui raizes, pois no intervalo citado a função não corta o eixo x.")