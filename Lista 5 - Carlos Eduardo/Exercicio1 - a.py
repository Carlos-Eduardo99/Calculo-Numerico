# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:43:25 2021

@author: Carlos
"""

import numpy as np

def eval_f (fx, x):
    return eval(fx)

def pontoFIXO(g,a,b,tol,n):
    x_anterior = float('nan')
    x = (a+b)/2
    for k in range(n):
        x_anterior = x
        x = eval_f(g,x)
        error = abs((x - x_anterior)/max(x,1))
        print(f'k={k}, x = {x:.5f}')
        if error < tol or x == x_anterior:
            print(f'Raiz aproximada encontrada: {x:.5f}')
            break
g = 'x - np.log(x)'
pontoFIXO(g,0.1,2,0.00001,20)

'''
- Por se tratar de uma função logarítmica não se pode isolar o x;

- Com isso, ao plotar o gráfico de g(x) e g'(x) nota-se que ambas são contínuas no intervalo
  e g'(x) < 1 no intervalo;

- Dessa forma todos os requisitos do teorema do ponto fixo foram atendidos e o método iterativo foi executado.

'''