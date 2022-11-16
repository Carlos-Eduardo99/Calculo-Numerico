# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:02:46 2021

@author: Carlos
"""

import numpy as np

def eval_f(fx, x):
    return eval(fx)

def pontoFixo(g, a, b, tol, n):
    xant = float("nan")
    x = ((a + b) / 2)
    for k in range(n):
        xant = x
        x = eval_f(g, x)
        erro = abs((x - xant) / max(x, 1))
        print(f'k = {k}, x = {x:.5f}')
        if erro < tol or x == xant:
            print(f'Raiz aproximada encontrada: {x:.5f}')
            break


equacao = str('(x*x+np.sin(x))')
g = 'x + 0.5 * (' + equacao + ')'
pontoFixo(g, -2, -0.5, 0.00001, 20)

'''
- Afim de evitar complicações com funções trigonométricas pode-se de imediato procurar valores para alfa.

- No entanto após ter utilizado inúmeros valores de alfa (0.01, 0.5, -0.5) pode-se notar que 
  as funções são contínuas no intervalo, porém g'(x) > 1.
  
- Após encontrar dificuldade em obter um valor  que atenda oo teorema, foi utilizado os valores de alfa
vistos anteriormente, porém com os 0.01 e 0,5 pode-se notar que a função não converge como esperado.

- Então neste caso foi utilizado o valor de alfa a = - 0.5

'''