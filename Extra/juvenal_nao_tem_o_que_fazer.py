# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:38:10 2018

@author: nelkisa.matias
"""

def f(n):
    if n == 1:
        g(1)
        return 1
    elif (n%2 == 0):
        g(1)
        f(n/2)
    else:
        g(1)
        f(3*n+1)

def g(x):
  global soma
  soma+=1
        
t = int(input())
saida = []

for vezes in range(t+1)[1::]:
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    for k in range(y+1)[x::]:
        soma = 0
        f(k)
        if k == x:
            maior = soma
        else:
            if soma>maior:
                maior = soma
    saida.append(maior)
  
for vezes in range(t+1)[1::]:
  print("Caso %d: %d" % (vezes,saida[vezes-1]))
    
    

