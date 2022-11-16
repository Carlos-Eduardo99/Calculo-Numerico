# -*- coding: utf-8 -*-
"""
Created on Mon Mar 1 10:57:13 2021

@author: Carlos
"""

import numpy as np

def linha_pivo(mat, lin, col):
    maior = abs(M[lin,col])
    lin_pivo = lin
    n = np.alen(M)
    for i in range(lin, n):
        if abs(M[i,col]) > maior:
            maior = abs(M[i,col])
            lin_pivo = i
    
    return lin_pivo

def troca_linha(M, lin1, lin2):
    if lin1 != lin2:
        print('Troca de linhas: ', lin1, '<->', lin2)
        aux = np.copy(M[lin1, :])
        M[lin1, :] = np.copy(M[lin2, :])
        M[lin2, :] = aux
        print(M)

def resolve_diag_sup(M):
    n = np.alen(M)
    b = np.copy(M[:,n])
    x = np.arange(n, dtype='double')
   # x[n-1] = b[n-1] / M[n-1, n-1]
    for i in range(n-2, -1, -1):
        soma = 0
        
        for j in range(i+1, n):
            soma += x[j] * M[i, j]
            x[i] = (b[i] - soma) / M[i, i]
    
    return x

def gauss_pivo(M):
    n = np.alen(M)
    for c in range(n-1):
        print('\n\nColuna', c)
        l = linha_pivo(M, c, c)
        troca_linha(M, l, c)
        pivo = M[c,c]
        
        for l in range(c+1, n):
            print('\nL{l} <- L{l} - L{c} * '.format(l=l, c=c) +
                  '{b} / {p}'.format(b=M[l,c], p=pivo))
            M[l, :] = M[l, :] - M[c, :] * M[l, c] / pivo
            print(M)

    return resolve_diag_sup(M)

def diag_Princ(M):
    aux=0
    for i in range (len(M)):
        for j in range (len(M[i])):
            if i == j:
                if (M[i, j]) == 0:
                    aux=1
                    
    return aux

def norma(M):
    print('L1: ', np.linalg.norm(M, 1))
    print('L2: ', np.linalg.norm(M, 2))
    print('Linf: ', np.linalg.norm(M, np.inf))
    
def condicionamento(M):
    print('Ordem 1: ', np.linalg.cond(M, 1))
    print('Ordem 2: ', np.linalg.cond(M, 2))
    print('Ordem infinito: ', np.linalg.cond(M, np.inf))
    
def fatora_lu(A):
    U = np.copy(A) 
    n = np.alen(U) 
    L = np.eye(n) 
    for j in range(n-1):
        for i in range(j+1, n):
            L[i, j] = U[i, j] / U[j, j] 
            for k in range(j, n):
                U[i, k] = U[i, k] - L[i, j] * U[j, k]
    return L, U

def resolve_diag_infLU(L, b):
    n = np.alen(L)
    y = np.arange(n, dtype='double') 
    y[0] = b[0] / L[0, 0] 
    for i in range(1, n):
        soma = 0
        for j in range(0, i):
            soma += y[j] * L[i, j]
        y[i] = b[i] - soma
    return y

def resolve_diag_supLU(U, y):
    n = np.alen(U)
    x = np.arange(n, dtype='double')
    x[n-1] = y[n-1] / U[n-1, n-1]
    for i in range(n-2, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += x[j] * U[i, j]
        x[i] = (y[i] - soma) / U[i, i]
    return x

M = np.array([
        [1, 8, -10, 0],
        [4, 5, 7, 0],
        [2, 16, -20, 0]
    ], dtype='double')
print('Matriz original: ')
print(M)

Ma = np.array([
        [1, 8, -10],
        [4, 5, 7],
        [2, 16, -20]
    ], dtype='double')

b = np.array([0, 0, 0], dtype='double')

g = gauss_pivo(M)

aux = diag_Princ(M)
if aux == 1:
    print("\nNão há solução! ")
else:
    print('\nObserva-se que não há zeros na diagonal principal, logo há solução: ')   
    print('\nNorma: ')
    norma(Ma)
    print('\nCondicionamentos: ')
    condicionamento(Ma)
    print('\nResolvendo por meio da fatoração LU: ')
    L, U = fatora_lu(Ma)
    y = resolve_diag_infLU(L, b)
    print('y =', y)
    x = resolve_diag_supLU(U, y)
    print('x =', x)