# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:00:22 2021

@author: Carlos
"""
from numpy import sqrt 

print('Informe abaixo os coefientes A, B e C da equação de segundo grau!')

a = float(input('Infome o valor do coeficiente de A : '))
b = float(input('Infome o valor do coeficiente do B : '))
c = float(input('Infome o  valor do coeficiente do C : '))



if a == 0:
    print('A equação não é de segundo grau!')
else:
    delta = (b ** 2 - 4 * a * c)
    if delta < 0:
        print('A equação não possuí raizes reais!')    
    elif (delta == 0):
        x = -b / (2 * a)
        print('A única raiz da equação de segundo é x = ' + str(x))
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print('Os valores das raizes da equação de segundo são: ')
        print('x1 = ' + str(x1))
        print('x2 = '+ str(x2))