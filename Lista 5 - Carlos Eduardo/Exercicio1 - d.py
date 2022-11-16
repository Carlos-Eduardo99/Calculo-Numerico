# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:29:07 2021

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
 - Inicialmente isolamos o x na equação e notamos que há convergencia x = (-x**2 - 1)/2
   x(0) = -2/2 = -1
   
 - g(x) = sqrt(-1/x - 2), por se tratar de um número negativo dentro de uma raiz, podemos constatar que no 
   intervalo [-2,0], esta função não é contínua.
 
 - Na tentativa de encontrar um alfa foi usado o a = 0.1, porém o g'(x) > 1;
 
 - Utilizando-se de um a = 0.5 o g'(x) > 1;
 
 - como houve dificuldade em encontrar um alfa que atendesse a condição, podemos usar uma função que não 
   atenda as condições.
 '''