# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 08:31:46 2021

@author: Carlos
"""
import numpy as np
def f(x):
    return (np.e**x)

def PosicaoFalsa(a, b, tol, n):
    xant = float("nan")
    for i in range(n):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        error=abs((x-xant)/max(x, 1))
        xant = x
        result = f(x)*f(a)
        fx = f(x)
        print("Iteração {i:3d}: a={a:+.5f}, ".format(i=i, a=a) +
              "b={b:+.5f}, error={err:+.5f}, ".format(b=b, err=error) +
              "x={x:+.5f}, f(x)={fx:+.5f}, ".format(x=x, fx=fx) +
              "f(x) x f(a)={r:+.5f}".format(r=result))
        if (fx == 0) or (error < tol):
            print("Raiz aproximada encontrada: {r:+5.5f}".format(r=x))
            break
        
        if (result) > 0:
            a = x
        else:
            b = x
        if (i == 19):
          print("Raiz aproximada encontrada: {r:+5.5f}".format(r=x))
          break
       
PosicaoFalsa(0, 5, 0.00001, 20)

print("Analisando o gráfico desta função através dos exercícios anteriores, podemos constatar que a mesma não possui raizes, pois no intervalo citado a função não corta o eixo x.")