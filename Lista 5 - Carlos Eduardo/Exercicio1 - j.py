# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:35:09 2021

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
        if error < tol or x == x_anterior or (k == 19):
            print(f'Raiz aproximada encontrada: {x:.5f}')
            break
g = 'x - (x- 3 - x**(-x))'
pontoFIXO(g,2,4,0.00001,20)

'''
- Isolando-se x na equação pode-se encontrar:
  g1(x): x = x ** -x + 3
  g2(x): x = (x**(x+1) - 1 )/3
  
- e considerando x(0) = (2+4)/2 = 3 nota-se que há convergencia

- Ao plotar o gráfico é possível constatar que g1(x) e g'(x) são contínuas ao intervalo.
  E também g'1(x) < 1. Com isso, pode-se executar o método do ponto fixo.

'''