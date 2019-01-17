def addVizinho(x, y):
    listaDeVizinhos[x - 1].append(y - 1)
    listaDeVizinhos[y - 1].append(x - 1)


def criarMatrizDistancias(numDeCidade):
    matriz = [[] for x in range(numDeCidade)]
    for cidade in range(len(matriz)):
        matriz[cidade] = [0 for x in range(numDeCidade)]
    return matriz


def addDistancia(x, y, distancia):
    matrizDistancia[x][y] = distancia
    matrizDistancia[y][x] = distancia


# MAIN

def menorCaminho(caminhos):
    menor = float("inf")
    listaMenor = 0
    for x in range(len(caminhos)):
        soma = sum(caminhos[x])
        if soma < menor:
            listaMenor = x+1
            menor = soma
    return listaMenor

def preencherDistancia(cidadeOrigem, linhaVizinhos, cidadeAtual, distancia=1, visitados=[]):
    visitados.append(cidadeAtual)
    for z in linhaVizinhos[cidadeAtual]:
        if z not in visitados:
            addDistancia(cidadeOrigem, z, distancia)
            preencherDistancia(cidadeOrigem, linhaVizinhos, z, distancia + 1, visitados)
        else:
            return


count = 1
while True:
    numCidades = int(input())
    listaDeVizinhos = [[] for n in range(numCidades)]
    matrizDistancia = criarMatrizDistancias(numCidades)

    for n in range(numCidades - 1):
        x, y = input().split()
        addVizinho(int(x), int(y))

    for x in range(numCidades):
        preencherDistancia(x, listaDeVizinhos, x, 1, [])

    print("Teste ", count)
    print(menorCaminho(matrizDistancia))
    print()
    count+=1