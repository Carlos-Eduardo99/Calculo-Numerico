# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:13:28 2021

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
g = 'x - 0.01 * (np.e**x - x**2 - 10)'
pontoFIXO(g,-10,5,0.00001,20)

'''
- Isolando-se o x na equação encontra-se

 g1(x): x = ln(x** - 10)
 g2(x): x = sqrt(e**x - 10)
 
- Agora aplicando x(0) = (-10+5)/2 = -2.5 nota-se que há convergência

- Ao plotar g1(x) e g2(x) juntamente com suas derivadas
  nota-se que elas não são contínuas no intervalo.
  
- Utilando-se do valor de a = 0.01 pode-se notar que g3(x) e g'3(x) são contínuas e
  g'3(x) < 1, ou seja, atendem os requisitos do teorema. Com isso podemos executar o método do ponto fixo.
  
'''