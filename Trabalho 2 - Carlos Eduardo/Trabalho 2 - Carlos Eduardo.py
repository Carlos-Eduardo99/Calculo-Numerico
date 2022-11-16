# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 11:48:53 2021

@author: Carlos
"""

import numpy as np

# Responsável por preencher os itens na matriz
def le_matriz(n):
    M = []
    print('\nInforme a matriz estendida ')
    print('(linha por linha e separando os números por vírgula e espaço entre eles): ')
    for i in range(n):
        lin = input('Linha {i}: '.format(i=i+1))
        lin_num = lin.split(',')
        lin_num = [float(i) for i in lin_num]
        M.append(lin_num)
    
    M = np.array(M, dtype='double')
    return M

def cria_vetor(n): #cria o vetor x0 com os valores iniciais das variáveis
    x0 = []
    for i in range(n):
        x0.append(0) #iniciando com 0 de forma padrão
    
    return x0

#Verifica se o sistema possuí solução, através da busca de zeros na diagonal principal.
def diag_Princ(M):
    aux=0
    for i in range (len(M)):
        for j in range (len(M[i])):
            if i == j:
                if (M[i, j]) == 0:
                    aux=1                    
    return aux
# Procura linha pivô em M na coluna col a a partir da linha lin
def linha_pivo(mat, lin, col):
    # Maior valor como o primeiro elemento
    maior = abs(mat[lin, col])
    # Linha pivo como a linha do primeiro elemento
    lin_pivo = lin
    # nlin é o número de linhas de M
    nLin = np.alen(mat)
    # Percorremos a coluna col a partir de lin
    for i in range(lin, nLin):   
        # Se o elemento da linha atual for maior
        if(abs(mat[i, col]) > maior):
            # Atualizamos o pivô
            maior = abs(mat[i, col])
            lin_pivo = i    
    return lin_pivo
# Troca lin1 e lin2 de M
def troca_linha(mat, lin1, lin2):
    # Testa se a linhas são diferentes
    if lin1 != lin2:
        print('Troca de linha - L{} <-> L{}'.format(lin1+1, lin2+1))
        aux = np.copy(mat[lin1, :])
        mat[lin1, :] = np.copy(mat[lin2, :])
        mat[lin2, :] = aux
        print(mat, '\n')  

# Resolve matriz M no formato de diagonal superior            
def resolve_diag_sup(mat):
    # n é o número de linhas de M
    n = np.alen(mat)
    # b é o vertor de termos constantes
    b = np.copy(mat[ : ,n])
    # Cria vetor x para guardar a solução
    x = np.arange(n, dtype='double')
    # Última linha já está isolada
    # x_n = b_n / M_n,n
    x[n-1] = b[n-1] / mat[n-1, n-1]
    
    # Percorre as linhas (em ordem decrescente, ignorando a última)
    for i in range(n-2, -1, -1):
        soma = 0
        # Soma as icógnitas já resolvidas (depois da diagonal)
        for j in range(i+1, n):
            soma += x[j] * mat[i, j]
   
        # x_i = (b_i - (soma das icógnitas)) / M_i,i
        x[i] = (b[i] - soma) / mat[i, i]    
    return x  

# Eliminação gaussiana com pivotamento          
def gauss_pivo(MA):
    mat = np.copy(MA)
    # n é o número de linhas de M
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

def jacobi(A, b, x0, tol, iteracoes):
    n = np.alen(A) # n é o número de linhas
    x = np.zeros(n, dtype='double') # Solução atual
    xant = x0 # Solução da iteração anterior
    
    for k in range(iteracoes): # Iterações do método
        for i in range(n): # Iterações para cada incógnita
            x[i] = b[i] # Termo constante
            for j in range(i): # Incógnitas anteriores
                x[i] -= A[i,j]*xant[j]
                
            for j in range(i+1, n): # Incógnitas posteriores
                x[i] -= A[i,j]*xant[j]
                
            x[i] /= A[i,i]  # Divisão pelo coeficiente da incógnita atual
        erro = np.linalg.norm(x-xant, np.inf) # Cálculo do erro
        
        print("Iteração {:3d}: ".format(k+1) +
              "x={}, ".format(x) +
              "Erro= {:8f}".format(erro))
        
        if (erro < tol):# Testa se erro é menor que a tolerânci 
            return x      
        xant = np.copy(x) # Copia solução atual para ser a anterior na próxima iteração      
    return x

# Laço de repetição resposável por controlar o ajuste do sistema
while(True):
    n = int(input('Informe o número de variáveis do sistema: '))
    M = le_matriz(n)
    tol = float(input('Informe a tolerância : '))
    ni = int(input('Informe o número de iterações: '))
    x0 = cria_vetor(n) #cria vetor de valores iniciais das variaveis
    Mq = np.delete(M, (n), axis=1) #matriz quadrada
    b = np.copy(M[:,n]) #vetor de termos constantes

    print("-"*50) 
    print('Matriz estendida original')
    print("-"*50)
    print(M, '\n')
    continua = input('Deseja ajustar o sistema[S/N]: ')
    
    if continua == 'N':
        break # interrompe o laço de repetição

#Escalonamento por gauss    
mat = gauss_pivo(M)

aux = diag_Princ(mat) #chama a função que verifica se a matriz possuí zeros na diagonal principal
if aux == 1: #testa se foram encontrados zeros na diagonal principal
    print("\nNão há solução! ")
else:
    #Definindo matriz A = L D U
    D = np.diag(np.diag(Mq))
    L = np.tril(Mq) - D
    U = np.triu(Mq) - D
    TJ = -np.linalg.inv(D).dot(L+U)
    avj, _ = np.linalg.eig(TJ) # Autovalores de TJ
    raioTJ = max(abs(avj)) 
# Verifica se o raio espectral converge
if (raioTJ < 1):
    print('Raio matriz -  TJ: {:5f}'.format(raioTJ))
    print('Método Jacobi: ')
    print('Solução:', jacobi(Mq, b, x0, tol, ni)) # Executa o método de Jacobi
else:
    print('\n Não converge! ')
