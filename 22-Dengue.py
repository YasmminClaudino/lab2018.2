def buscar(cidadeOrigem, linhaVizinhos, cidadeAtual, distancia=1, visitados=[]):
    for z in linhaVizinhos[cidadeAtual]:
        visitados.append(cidadeAtual)
        if z not in visitados:
            addDistancia(cidadeOrigem, z, distancia)
            buscar(cidadeOrigem, linhaVizinhos, z, distancia + 1, visitados)
        else:
            return
def addDistancia(x, y, distancia):
    caminhos[x][y] = distancia
    caminhos[y][x] = distancia

def montarMatriz(caminhos,qtd):
    for i in range(qtd):
        caminhos.append([0] * qtd)

def menorCaminho(caminhos):
    menor = float("inf")
    for x in range(len(caminhos)):
        soma = sum(caminhos[x])
        if soma < menor:
            menor = soma
    return (x+1)

count = 1
while True:
    qtd = int(input())
    if qtd == 0:
        break
    caminhos = []
    lista = [[] for x in range(qtd)]
    for i in range(qtd-1):
        a, b = [int(n) for n in input().split()]
        lista[a - 1].append(b - 1)
        lista[b - 1].append(a - 1)
    montarMatriz(caminhos,qtd)
    for x in range(qtd):
        buscar(x, lista, x, 1, [])

    print("Teste %s" % count)
    print(menorCaminho(caminhos))
    print()
    count += 1