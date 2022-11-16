# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:52:08 2021

@author: Carlos
"""
from numpy import sqrt

A = float(input("Informe o valor de A:"))
B = float(input("Informe o valor de B:"))
C = float(input("Informe o valor de C:"))

N = ((A + B * C) - sqrt(A * B * C)) / (2 * C + B)

print('O valor de N = ' + str(N))