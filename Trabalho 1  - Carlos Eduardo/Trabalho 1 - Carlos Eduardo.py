# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:36:20 2021

@author: Carlos
"""

import numpy as np
import matplotlib.pyplot as plot

#Função responsável por calcular a função e intervalo passados
def eval_f(fx ,x):
    return eval(fx)

#Procedimento responsável por plotar o gráfico da função
def grafico(fx, a, b):
# Gera os ponto do intervalo e preenche a variável intervalo   
    intervalo = np.linspace(a,b)  
    plot.plot(intervalo, eval_f(fx,intervalo), label = 'f(x)')
    plot.legend()
    plot.grid() 
    plot.show() #mostra o gráfico


# Definição da função para a qual buscamos a raiz
def f(x, funcao):
    return eval(funcao)

# Método da bisseção
def bissecao(a, b, tol, n, funcao):
# Inicialmente, não temos um x anterior
    xant = float("nan")
# Laço de repetição com as iterações
    for i in range(n):
# Calcula x (ponto no meio do intervalo [a, b])
        x = (a + b) / 2
        fx = f(x, funcao)
        sinal = f(a, funcao) * fx
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
            break
# Verifica se o sinal de f(a) * f(x) é menor que zero
        if sinal > 0:
# Em caso afirmativo, o próximo intervalo será [x, b]
           a = x
        else:
# Senão, o próximo intervalo será [a, x]
           b = x

#Método da Posição Falsa
def posicaoFalsa(a, b, tol, n, funcao):
    xant = float("nan")
    for i in range(n):
        x = (a * f(b, funcao) - b * f(a, funcao)) / (f(b, funcao) - f(a, funcao))# Calcula x**(k)
        # Cálculo do erro relativo
        error=abs((x-xant)/max(x, 1))
        xant = x
        result = f(x, funcao)*f(a, funcao)
        fx = f(x, funcao) # Atualiza x**(k−1)
        # Mostra as informações da iteração atual
        print("Iteração {i:3d}: a={a:+.5f}, ".format(i=i, a=a) +
              "b={b:+.5f}, error={err:+.5f}, ".format(b=b, err=error) +
              "x={x:+.5f}, f(x)={fx:+.5f}, ".format(x=x, fx=fx) +
              "f(x) x f(a)={r:+.5f}".format(r=result))
        if (fx == 0) or (error < tol): # Testa o critério de parada
            # Exibe a raiz encontrada
            print("Raiz aproximada encontrada: {r:+5.5f}".format(r=x))
            break
        
        if (result) > 0: # Testa se a raiz está entre x e b
            a = x
        else: # Ou entre a e x
            b = x
        if (i == 19):
          print("Raiz aproximada encontrada: {r:+5.5f}".format(r=x))
          break

# Método da secante
def secante(a, b ,Tol, n, funcao):
# Inicialmente, não temos um x anterior
    x_anterior = float("NaN")
    x = a
    x_anterior = b 
    for k in range(0,n):
        # Cálculo do erro relativo
        error = abs ((x-x_anterior)/(max(x,1)))
        print(k,x,f(x, funcao), error)
        
        if f(x, funcao) == 0 or error < Tol: # Testa o critério de parada
            break
        xa = x - f(x, funcao) * ((x-x_anterior)/ f(x, funcao) -f(x_anterior, funcao)) #  Calcula x**(k+1)
        x_anterior = x # Atualiza x**(k−1)
        x = xa # Atualiza x**(k+1)
    return x
    print(f'Raiz aproximada encontrada: {(secante(a, b, tol, n)):.5f}')   

# Laço de repetição responsável por manter o usuário no programa
while(True):

# Coleta dos requisitos para a plotagem do gráfico e cálculo da raiz
    print('======== SISTEMA DE RESOLUÇÃO DE EQUAÇÕES NÃO LINEARES ========')
    fx = input('Informe a função f(x): ')

# Laço de repetição resposável por controlar o ajuste do intervalo
    while (True):

        a = float(input('Informe o início do intervalo: '))
        b = float(input('Informe o fim do intervalo: '))
# Chama a função que plotará o gráfico
        grafico(fx, a, b)
    
        continua = input('Deseja ajustar o intervalo[S/N]: ')
# Caso o usuário digite S o laço de repetição é mantido, do contrário a raiz é calculada
        if continua == 'N':
            break # interrompe o laço de repetição

# Definindo os valores de tolerancia e o número de itelações, os quais serão passados por parâmetro
    tol = 0.00001
    n = 20

    print('')
    print('=============== CÁLCULO DA RAIZ PELO MÉTODO DA BISSEÇÃO ======================')
# Chama a função bissecao que executa o método da bisseção
    bissecao(a, b, tol, n, fx)
    print('===================================================================================')
    print('')
    print('=============== CÁLCULO DA RAIZ PELO MÉTODO DA POSIÇÃO FALSA ======================')
# Chama a função posicaoFalsa que executa o método da Posição Falsa
    posicaoFalsa(a, b, tol, n, fx)
    print('===================================================================================')
    print('')
    print('=============== CÁLCULO DA RAIZ PELO MÉTODO DA SECANTE ======================')
# Chama a função secante que executa o método da Secante
    secante(a, b, tol, n, fx) 
    print('===================================================================================')
    
    continua = input('Deseja realizar um novo cálculo [S/N]: ')
    if continua == 'N': # Verifica se o usuário deseja ou não realizar o programa novamente
        break # Interrompe o programa