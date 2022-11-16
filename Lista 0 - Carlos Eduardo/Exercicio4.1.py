# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:38:54 2021

@author: Carlos
"""
h = int(input('Informe a quantidade de horas: '))
m = int(input('Informe a quantidade de minutos: '))
s = int(input('Informe a quantidade de segundos: '))

s = h * 60 * 60 + m * 60 + s

print('O total de segundos é {:d}'.format(s))