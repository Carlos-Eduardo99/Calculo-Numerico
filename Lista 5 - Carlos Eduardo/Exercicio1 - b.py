# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:08:06 2021

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
g = 'x - 0.5 * np.e**x'
pontoFIXO(g,0,5,0.00001,20)
print("Analisando o gráfico desta função através dos exercícios anteriores, podemos constatar que a mesma não possui raizes, pois no intervalo citado, a função não corta o eixo x.")