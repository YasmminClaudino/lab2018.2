#funções
def constroiQuadrado(tamanho,lista):
    for guarda in range(tamanho):
        valores = [int(valores) for valores in input().split()]
        lista.append(valores)
    return lista
def validacao(soma, valorA, valorB,x,tamanho):
    if soma == valorA:
        return (valorA, x, valorB)
    else:
        if x == tamanho-1:
            return (valorA, x, valorB)
        return (valorB, x-1, valorA)

def achaM(lista, tamanho):
    valorA = sum(quadrado[0])
    for x in range(1,tamanho):
        valorB = sum(quadrado[x])
        if valorB == valorA:
            continue
        else:
            if x != tamanho-1:
                soma = sum(quadrado[x+1])
            else:
                soma = sum(quadrado[x])
        return validacao(soma,valorA,valorB,x,tamanho)

def verificaColuna(quadrado,m, tamanho,linhaErrada):
    j = 0
    for linha in range(tamanho):
        soma, i = 0,0
        for coluna in range(tamanho):
            soma += quadrado[i][j]
            i += 1
        if soma != m:
            nErrado = quadrado[linhaErrada][j]
            return nErrado
        j+=1
    return nErrado

def numeroCerto(somaErrada,m, nErrado):
    nCerto = (nErrado + m) - somaErrada
    return nCerto

#main
tamanhoQuadrado = int(input())
quadrado = []
m = 0

constroiQuadrado(tamanhoQuadrado,quadrado)
achaVM = achaM(quadrado,tamanhoQuadrado)
m = achaVM[0]
linhaErrada = achaVM[1]
somaErrada = achaVM[2]
nErrado = verificaColuna(quadrado, m, tamanhoQuadrado, linhaErrada)
nCerto = numeroCerto(somaErrada,m,nErrado)
print("%d %d" %(nCerto, nErrado))