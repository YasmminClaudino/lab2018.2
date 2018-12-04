tamanhoMatriz = int(input())
quadrado = []
resultado = 0

for tamanho in range(tamanhoMatriz):
    valores = [int(valores) for valores in input().split()]
    quadrado.append(valores)

resultado = sum(valores)

def verificaSoma(soma,resultado):
    if soma == resultado:
        return resultado
    else:
        return -1

def verificaDiagonalEsquerda(lista,tamanhoMatriz):
    soma = 0
    i = 0
    j = 0
    for linha in range(tamanhoMatriz):
        for coluna in range(1):
            soma += lista[i][j]
            j+=1
        i+=1
    return soma
def verificaDiagonalDireita(lista, tamanhoMatriz):
    soma = 0
    i = 0
    j = tamanhoMatriz-1
    for linha in range(tamanhoMatriz):
        for coluna in range(1):
            soma += lista[i][j]
            j-=1
        i+=1
    return soma

def verificaLinha(lista, tamanhoMatriz, resultado):
    soma = 0
    i = 0
    j = 0
    for todasLinhas in range(tamanhoMatriz):
        for linha in range(tamanhoMatriz):
            for coluna in range(1):
                soma += lista[i][j]
            j+=1
        if verificaSoma(soma, resultado) == resultado:
            i+=1
            j = 0
            soma = 0
        else:
            return -1
    return resultado

def verificaColuna(lista, tamanhoMatriz, resultado):
    soma = 0
    i = 0
    j = 0
    for todasColunas in range(tamanhoMatriz):
        for linha in range(1):
            for coluna in range(tamanhoMatriz):
                soma += lista[i][j]
                i+=1
            if verificaSoma(soma, resultado) == resultado:
                j+=1
                i = 0
                soma = 0
            else:
                return -1
    return resultado
while True:
    if verificaSoma(verificaDiagonalEsquerda(quadrado, tamanhoMatriz), resultado) != resultado:
        print(-1)
        break
    elif verificaColuna(quadrado, tamanhoMatriz, resultado) != resultado:
        print(-1)
        break
    elif verificaLinha(quadrado,tamanhoMatriz, resultado) != resultado:
        print(-1)
        break
    elif verificaSoma(verificaDiagonalDireita(quadrado, tamanhoMatriz), resultado) != resultado:
        print(-1)
        break
    else:
        print(resultado)
        break