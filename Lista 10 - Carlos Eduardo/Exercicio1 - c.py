# -*- coding: utf-8 -*-
"""
Created on Tue Mar 09 11:00:46 2021

@author: Carlos
"""
import numpy as np

def cria_colunas(x, y, n, T):
    flag = 0
    k = 1
    for j in range(1, n):
        for i in range(k, n):
            if ((x[i] - x[i-k])):
                T[i,j] = (T[i,j-1] - T[i-1,j-1])/(x[i] - x[i-k])
            else:
                flag = 1
        k = k+1
        print('\n{j}ª coluna:\n'.format(j=j+1), T)
        
    return flag

def poli(n):
    # Polinômio interpolador
    print('-----------------------------------------------')
    print('\nPolinômios menores:')

    pm = []
    p = []
 
    for cont in range(n):
        if cont == 0:
            pm.append(np.poly1d(1))
            print(pm[cont])
            p.append(pm[cont])            
        else:
            pm.append(np.poly1d([1, -x[cont-1]]))
            print(pm[cont])
            p.append(np.polymul(pm[cont], p[cont-1]))
           
    for cont in range(n):
       print('-----------------------------------------------')
       print('\np{cont}:\n'.format(cont=cont), p[cont])
       
    for cont in range(n):
        if cont == 0:
            p[cont]=np.polymul(p[cont], T[cont, cont])
            pf = p[cont]
        else:
            p[cont]=np.polymul(p[cont], T[cont, cont])
            pf = pf + p[cont]
    
    for cont in range(n):
        print('-----------------------------------------------')
        print('\np{cont}*a{cont1}:\n'.format(cont=cont,cont1=cont+1),p[cont])
   
    return pf

def lagrange(n):
    l = []
    for j in range(n):
        d = 1
        pxn = []
        for i in range (n):
            if i != j:
                # Denominador
                d = d * (x[j] - x[i])
                # Numerador
                pxn.append(np.poly1d([1, -x[i]]))
        if (d == 0):
            p = 0
            return p
        for cont in range(n-2):
            if cont == 0:
                px = np.polymul(pxn[cont], pxn[cont+1])
            else:
                px = np.polymul(px, pxn[cont+1])
      
        l.append(np.polydiv(px, d)[0])
        print('-----------------------------------------------')
        print('L{j}:\n'.format(j=j), l[j])
        
    for cont in range(n-1):
        if cont == 0:
            p = np.polymul(l[cont], y[cont]) + \
                np.polymul(l[cont+1], y[cont+1]) 
        else:
            p = p + np.polymul(l[cont+1], y[cont+1])
    
    return p
        
x = np.array([-5, -3, 1, 4, 7, 10], dtype='double')
y = np.array([2, 4, 5, -6, -9, -15], dtype='double')
n = 6

# Inicializa tabela
T = np.zeros((n, n))

print("Resolvendo por Divididas de Newton: ")

# Primeira coluna
T[:,0] = y
print('\n1ª coluna:\n', T)

aux = cria_colunas(x, y, n, T)

if (aux==1):
    print('\nHouve um erro e Divididas de Newton não consegue resolver!')
else:
    pf = poli(n)
    print('-----------------------------------------------')
    print('\nPolinômio Interpolador encontrado por Divididas de Newton:\n', pf)
    
print("\nResovendo por Lagrange: ")

p = lagrange(n)

if (p == 0):
    print('Houve um erro e Lagrange não consegue resolver!')
else:
    print('-----------------------------------------------')
    print('Polinômio Interpolador encontrado por Lagrange:\n', p)
