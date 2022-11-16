# -*- coding: utf-8 -*-
"""
Created on Tue Feb 9 15:22:38 2021

@author: Carlos
"""
import numpy as np
# Definição da função para a qual buscamos a raiz
def f(x):
    return (np.e**x)
# Método da bisseção
# Recebe o intervalo [a, b] a tolerância e o número máximo de iterações
def bissecao(a, b, tol, n):
# Inicialmente, não temos um x anterior
    xant = float("nan")
# Laço de repetição com as iterações
    for i in range(n):
# Calcula x (ponto no meio do intervalo [a, b])
        x = (a + b) / 2
        fx = f(x)
# O Sinal é f(a) * f(x)
        sinal = f(a) * fx
# Cálculo do erro relativo
        error=abs((x-xant)/max(x, 1))
# x anterior (será usado na próxima iteração)
        xant = x
# Mostra as informações da iteração atual
        print("Iteração {i:3d}: a={a:+.5f}, ".format(i=i, a=a) +
              "b={b:+.5f}, error={err:+.5f}, ".format(b=b, err=error) +
              "x={x:+.5f}, f(x)={fx:+.5f}, ".format(x=x, fx=fx) +
              "sinal={s:+.5f}".format(s=sinal))
# Testa a condição de parada: f(x) = 0 ou tolerãncia < erro
        if (fx == 0) or (error < tol):
# Exibe a raiz encontrada
            print("Raiz aproximada encontrada: {r:+5.5f}".format(r=x))
# Interrompe o laço de repetição
            break
# Verifica se o sinal de f(a) * f(x) é menor que zero
        if sinal > 0:
# Em caso afirmativo, o próximo intervalo será [x, b]
           a = x
        else:
# Senão, o próximo intervalo será [a, x]
           b = x
# Executa o métido da bisseção
bissecao(0.5, 1.5, 0.00001, 20)