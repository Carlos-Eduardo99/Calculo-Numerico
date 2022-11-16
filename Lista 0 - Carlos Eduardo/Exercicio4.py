# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:28:44 2021

@author: Carlos
"""
s = int(input("Informe a quantitade de segundos: "))

m = s // 60

s = s % 60

h = m // 60

m = m % 60

print('Horas: {:d}', format(h))
print('Minutos: {:d}', format(m))
print('Segundos: {:d}', format(s))