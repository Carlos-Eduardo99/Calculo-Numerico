# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:51:12 2021

@author: Carlos
"""
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
g = 'x - 1/3 * (x**3 + 3*x - 1)'
pontoFIXO(g,-5,5,0.00001,20)

'''
- Ao isolar o x na equação encontrei:
    g1(x): x = (-3**x + 1) ** 1/3
    g2(x): x = (-x**3 + 1)/3

- e x(0) =( -5 +5 ) / 2 = 0  podemos notar que há convergência

- quando plota -se o gráfico de g1 juntamente com sua derivada
  pode-se notar que a função não é contínua

- Já o gráfico de g2, tanto g2 quanto g'1 são contínuas, no entanto g'2(x) > 1 no intervalo.

- Como houve dificuldade em encontrar um alfa que atenda ao teorema, utilizei um alfa no valor de 1/3

'''