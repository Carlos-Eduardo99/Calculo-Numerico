# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 14:50:25 2021

@author: Carlos
"""

num = 1*2**6 + 1*2**4 + 1*2**1 + 1*2**-2 + 1*2**-3
print("Na base 10: ",num)

#convertendo para base 4 
list = []
listA = []
resto  = 2
numInt = 82
numFrac = 0.375
cont = 0
while numInt != 0:
    
    resto = numInt % 4 ; numInt = numInt // 4; list.append(resto);     

while cont < 8:

    resto2 = numFrac * 4; numFrac = resto2 - int(resto2); listA.append(int(resto2));
    cont = cont + 1

listA.reverse()     
list.reverse()    
print("Na base 4: ",*list,".",*listA, sep=" ")

#convertendo para octal
list = []
listA = []
resto  = 2
numInt = 82
numFrac = 0.375
cont = 0
while numInt != 0:
    
    resto = numInt % 8 ; numInt = numInt // 8; list.append(resto);     

while cont < 8:

    resto2 = numFrac * 8; numFrac = resto2 - int(resto2); listA.append(int(resto2));
    cont = cont + 1

listA.reverse()    
list.reverse()    
print("Na base 8: ",*list,".",*listA, sep=" ") 

#convertendo para hexadecimal
numInt = 82
Numfrac = 375
List2 = []
List3 = []
print("Na base 16: ")
while numInt > 0:
    List2.append(numInt % 16)
    numInt = numInt // 16

for i in range(len(List2)-1,-1,-1):      
    
    print("%X"%List2[i],end="")       

while Numfrac > 0:
    List3.append(Numfrac % 16)
    Numfrac = Numfrac // 16

for i in range(len(List3)-1,-1,-1):

    print("%X"%List3[i],end="")
