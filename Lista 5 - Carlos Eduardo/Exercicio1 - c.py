# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:18:57 2021

@author: Carlos
"""
import numpy as np

def eval_f (fx, x):
    return eval(fx)

def pontoFIXO(g,a,b,tol,n):
    x_anterior = float('nan')
    x = ((a+b)/2)
    for k in range(n):
        x_anterior = x
        x = eval_f(g,x)
        error = abs((x - x_anterior)/max(x,1))
        print(f'k={k}, x = {x:.5f}')
        if error < tol or x == x_anterior:
            print(f'Raiz aproximada encontrada: {x:.5f}')
            break
g = 'x + 0.5 * (np.cos(x))'
pontoFIXO(g,1,2,0.00001,20)

'''
- Afim de evitar complicações com funções trigonométricas pode-se de imediato procurar valores para alfa.

- Na tentativa de encontrar um alfa foi usado o a = 0.1,no entanto ao plotar o gráfico
  nota-se que g(x) e g'(x) são contínuas no intervalo, porém o g'(x) > 1; Com isso os requisitos não são atendidos
  e um novo valor deve ser obtido;

- Agora utilizando-se de a = -0.5 pode-se verificar que g'(x) < 1, dessa forma o metodo iterativo pode
  ser executado.

'''