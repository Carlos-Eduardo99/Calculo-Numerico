# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 19:56:57 2021

@author: Carlos
"""
while (True):
    op = input('Informe a operação(+, -, *, /, **): ')
    if op not in ['+' , '-', '*' , '/' , '**']:
        print('Operação inválida! Tente novamente!')
    else:
        print('Informe dois números:')
        n1 = float(input('n1 = '))
        n2 = float(input('n2 = '))
    
    if op == '+':
        r = n1 + n2
        print('Resultado: {:e}'.format(r))
    elif op == '-':
        r = n1 - n2
        print('Resultado: {:e}'.format(r))
    elif op == '*':
        r = n1 * n2
        print('Resultado: {:e}'.format(r))
    elif op == '/':
        r = n1/n2
        print('Resultado: {:e}'.format(r))
    elif op == '**':
        r = n1 ** n2
        print('Resultado: {:e}'.format(r))

    continua = input('Deseja continuar(s/n): ')
    if continua == 'n':
        break
        

    
    
