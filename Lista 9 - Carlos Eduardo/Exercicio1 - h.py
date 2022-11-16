# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:14:00 2021

@author: Carlos
"""
import numpy as np

#Define a linha que contem o maior elemento para ser o pivo
def linha_pivo(mat, lin, col):
    maior = abs(mat[lin, col])
    lin_pivo = lin
    nLin = np.alen(mat)
    
    for i in range(lin, nLin):    
        if(abs(mat[i, col]) > maior):
            maior = abs(mat[i, col])
            lin_pivo = i    
    return lin_pivo

def troca_linha(mat, lin1, lin2):
    if lin1 != lin2:
        print('Troca de linha - L{} <-> L{}'.format(lin1+1, lin2+1))
        aux = np.copy(mat[lin1, :])
        mat[lin1, :] = np.copy(mat[lin2, :])
        mat[lin2, :] = aux
        print(mat, '\n')  
              
def resolve_diag_sup(mat):
    n = np.alen(mat)
    b = np.copy(mat[ : ,n])
    x = np.arange(n, dtype='double')
    x[n-1] = b[n-1] / mat[n-1, n-1]
    
    for i in range(n-2, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += x[j] * mat[i, j]
            
        x[i] = (b[i] - soma) / mat[i, i]    
    return x  
          
def gauss_pivo(MA):
    mat = np.copy(MA)
    n = np.alen(mat)    
    for i in range(n-1):
        print("-"*50)
        print('Operações da coluna:', i+1)
        print("-"*50)
        l = linha_pivo(mat, i, i)
        troca_linha(mat, l, i)
        pivo = mat[i,i]
        for j in range(i+1, n):
            
            if (mat[j,i] != 0):
                print('L{j:} <- L{j:} - (L{i:} * '.format(j=j+1, i=i+1) +
                      '{})/{}'.format(mat[j,i], pivo))
                mat[j, :] = mat[j, :] - mat[i, :] * mat[j, i] / pivo
                print(mat, '\n')    
    return mat
def verif_solucao(mat):
    lin = np.alen(mat)
    test = True
    
    for i in range(lin):
        if(mat[i][i] == 0):
            test = False            
    return test

#Método Jacobi       
def jacobi(A, b, x0, tol, iteracoes):
    n = np.alen(A)
    x = np.zeros(n, dtype='double')
    xant = x0 
    
    for k in range(iteracoes): 
        for i in range(n): 
            x[i] = b[i] 
            
            for j in range(i): 
                x[i] -= A[i,j]*xant[j]
                
            for j in range(i+1, n): 
                x[i] -= A[i,j]*xant[j]
                
            x[i] /= A[i,i] 
        erro = np.linalg.norm(x-xant, np.inf) 
        
        print("Iteração {:3d}: ".format(k+1) +
              "x={}, ".format(x) +
              "Erro= {:8f}".format(erro))
        
        if (erro < tol): 
            return x      
        xant = np.copy(x)        
    return x

#Método Gauss-Seidel       
def gauss_seidel(A, b, x0, tol, iteracoes):
    n = np.alen(A) 
    x = np.zeros(n, dtype='double') 
    xant = x0 
    
    for k in range(iteracoes): 
        for i in range(n): 
            x[i] = b[i] 
            
            for j in range(i): 
                x[i] -= A[i,j]*x[j]
                
            for j in range(i+1, n): 
                x[i] -= A[i,j]*xant[j]
        
            x[i] /= A[i,i] 
        erro = np.linalg.norm(x-xant, np.inf) 
        
        print("Iteração {:3d}: ".format(k+1) +
              "x={}, ".format(x) +
              "Erro= {:8f}".format(erro))
        
        if (erro < tol): 
            return x
        xant = np.copy(x)        
    return x

#Define a matriz ampliada
MA = np.array([
        [7, 1, -2, 2, 2.38],
        [1, 14, -3, 2, 5.06],
        [1, -2, 13, 3, 6.88],
        [2, 2, 1, 9, 6.54]
        ], dtype='double')


print("-"*50) 
print('Matriz estendida original')
print("-"*50)
print(MA, '\n')

#Escalonamento por gauss
mat = gauss_pivo(MA)
#Retorna se o sistema escalonado possui 0 na diagonal principal:
test = verif_solucao(mat)

#verifica se o sistema possui solução
if test == True:
    
    n = np.alen(MA)
    MC = np.copy(MA[:, 0:n])
    b = np.copy(MA[:, n:n+1])
    x0 = np.array([0, 0, 0, 0], dtype='double')
    
    #Resolve o sistema escalonado com pivotamento
    x = resolve_diag_sup(mat)
    print('Solução com pivotamento:')
    n = np.alen(x)
    print('[ ', end = '')
    for i in range(n):
        print('{}'.format(x[i]), end = ',  ')
    print(']')
    
    #Definindo matriz A = L D U
    D = np.diag(np.diag(MC))
    L = np.tril(MC) - D
    U = np.triu(MC) - D
    
    TJ = -np.linalg.inv(D).dot(L+U)
    TG = -np.linalg.inv(L+D).dot(U)
   
    avj, _ = np.linalg.eig(TJ) 
    avg, _ = np.linalg.eig(TG)
    raioTJ = max(abs(avj)) 
    raioTG = max(abs(avg)) 
    print("-"*50)
    print('Método Jacobi e Gauss-Seidel')
    print("-"*50)
    print('Raio matriz -  TJ: {:5f}     TG: {:5f}'.format(raioTJ, raioTG))
    print("-"*50)
    print('Método Jacobi: ')
    print('Solução:', jacobi(MC, b, x0, 0.00001, 30))
    
    print('\n\nMétodo Gauss-Seidel: ')
    print('Solução:', gauss_seidel(MC, b, x0, 0.00001, 30))
else:
    print('Não existe solução!')
