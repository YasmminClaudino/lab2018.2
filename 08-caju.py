def constroeMatriz(linha, coluna, cajueiro):
    for y in range(linha):
        x = [int(x) for x in input().split()]
        cajueiro.append(x)
    return cajueiro

def constroeDinamica(lista,m,n,d,qtdL,qtdC):
    for i in range(1,qtdL+1):
        for j in range(1,qtdC+1):
            d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + cajueiro[i-1][j-1]


def enche0(d,m,n):
    for x in range(qtdL+1):
        linha = []
        for x in range(qtdC+1):
            linha.append(0)
        d.append(linha)


def maior(d,m,n,qtdL,qtdC):
    maior = 0
    for i in range(m, qtdL+1):
        for j in range(n,qtdC+1):
            t = (d[i][j] - d[i][j-n]) - d[i-m][j] + d[i-m][j-n]
            if t > maior:
                maior = t
    return maior

entrada = input().split()
cajueiro = []
d = []
qtdL,qtdC, m,n = int(entrada[0]),int(entrada[1]),int(entrada[2]), int(entrada[3])
constroeMatriz(qtdL,qtdC, cajueiro)
enche0(d,qtdL,qtdC)
constroeDinamica(cajueiro,m,n,d,qtdL,qtdC)

print(maior(d,m,n,qtdL,qtdC))
