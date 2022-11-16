# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:45:50 2021

@author: Luiz
"""

ano = int(input('Informe o ano: '))

if ((ano % 400) == 0) or (((ano % 4) == 0) and ((ano % 100) !=0)):
    print('O ano de ' + str(ano) + ' é bissexto!')
else:
    print('O ano de ' + str(ano) + ' não é bissexto!')