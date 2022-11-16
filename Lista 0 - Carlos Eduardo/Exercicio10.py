# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:13:44 2021

@author: Carlos
"""
n = int (input('Informe a quantidade de elementos do conjunto: '))

for i in range(n):
    for j in range(n):
        for k in range(n):
            print('({:d} , {:d}, {:d})'.format(i+1, j+1, k+1))