# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:40:18 2021

@author: Carlos
"""
import numpy as np


def eval_f(fx, x):
    return eval(fx)


def pontoFixo(g, a, b, tol, n):
    x_anterior = float('nan')
    x = ((a + b) / 2)
    for k in range(n):
        x_anterior = x
        x = eval_f(g, x)
        erro = abs((x - x_anterior) / max(x, 1))
        print(f'k = {k}, x = {x:.5f}')
        if erro < tol or x == x_anterior:
            print(f'Raiz aproximada encontrada: {x:.5f}')
            break


g = str('x - 0.5 * (x**2 +2*x+1)')
pontoFixo(g, -2, 0, 0.00001, 20)

'''
 - Isolando-se o x nessa equeção encontraremos: 
    g1(x): x = sqrt(-2*x - 1)
    g2(x): x = (-x**2 - 1)/2

- Levando em consideração o exercício anterior podemos notar que se tratam das mesmas função,
então podemos utiliza-las novamente
'''