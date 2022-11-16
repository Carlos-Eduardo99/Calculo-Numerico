# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:17:17 2021

@author: Carlos
"""
print('Informe dois números')
n1 = int(input('Primeiro número: '))
n2 = int (input('Segundo número: '))

n1_copia = n1
n2_copia = n2
while(True):
    r = n1 % n2
    if r == 0:
        mdc = n2
        break
    else:
        n1 = n2
        n2 = r

print ('O MDC é {:d}'.format(mdc))

mmc = (n1_copia * n2_copia) // mdc

print ('O MMC é {:d}'.format(mmc))