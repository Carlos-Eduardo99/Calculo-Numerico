# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 16:45:47 2021

@author: Carlos
"""

x = 1.00001 
y = 1

print("(a) O erro absoluto: ",abs(x-y),"Relativo: ",abs(x-y)/x)

x = 100001 
y = 100000

print("(b) O erro absoluto: ",abs(x-y),"                     Relativo: ",abs(x-y)/x)

x = 32.65483 
y = 34.1645

print("(c) O erro absoluto: ",abs(x-y),"    Relativo: ",abs(x-y)/x)


x = 5.87135 
y = 5.87049

print("(d) O erro absoluto: ",abs(x-y)," Relativo: ",abs(x-y)/x)