# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:24:51 2021

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
g = 'x - 0.01 * (np.sqrt(x) - np.cos(x))'
pontoFIXO(g,0,2,0.00001,20)

'''
- Afim de evitar complicações com funções trigonométricas pode-se de imediato procurar valores para alfa.

- Utilando-se do valor de a = 0.01 pode-se notar que g(x) e g'(x) são contínuas e
  g'(x) < 1, ou seja, atendem os requisitos do teorema. Com isso podemos executar o método do ponto fixo.
'''