# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 13:58:25 2021

@author: Carlos
"""

octal = 4*8**2 + 2*8**1 + 5*8**0+ 1*8**-1 + 3*8**-2 + 5*8**-3

binario = 1*2**6 + 0*2**5 + 0*2**4 + 1*2**3 + 1*2**2 + 0*2**1+ 1*2**0 + 1*2**-1 + 1*2**-2 + 0*2**-3 + 1*2**-4

hexa = 1*16**4 + 2*16**3 + 15*16**2 + 10*16**1 + 7*16**0 + 4*16**-1 + 12*16**-2 + 8*16**-3

print("O número 425.135 na base 8 em base decimal é: ",octal)
print("O número 1001101.1101 na base 2 em base decimal é: ",binario)
print("O número 12FA7.4C8  na base 16 em base decimal é: ",hexa) 