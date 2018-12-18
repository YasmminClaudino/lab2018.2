def menorElementoQ(q):
    menor = min(q, key=q.get)
    return menor
def dijkstra(grafo, destino):
    q = {}
    distancia = {}
    anterior = {}
    caminho = {}
    for vertice in grafo:
      distancia[vertice] = float("inf")
      anterior[vertice] = None
    distancia[destino] = 0
    q = distancia
    while len(q) != 0:
        u = menorElementoQ(q)
        caminho[u] = q.pop(u)
        for v in grafo[u]:
          distanciaTemporaria = caminho[u] + grafo[u][v]
          if v in q:
              if q[v] > caminho[u] + grafo[u][v]:
                q[v] = distanciaTemporaria
                anterior[v] = u
    return caminho

def preencheGrafo(qtdVoos,qtdCidades,grafo):
    for i in range(qtdVoos):
        voos = input().split(" ")
        if int(voos[0]) not in grafo:
          grafo[int(voos[0])]={int(voos[1]):int(voos[2])}
        else:
          if int(voos[1]) in grafo[int(voos[0])]:
            if grafo[int(voos[0])][int(voos[1])] > int(voos[2]):
              grafo[int(voos[0])][int(voos[1])]= int(voos[2])
            else: pass
          else: grafo[int(voos[0])].update({int(voos[1]):int(voos[2])})
        #voltando:
        if int(voos[1]) not in grafo:
          grafo[int(voos[1])]={int(voos[0]):int(voos[2])}
        else:
          if int(voos[0]) in grafo[int(voos[1])]:
            if grafo[int(voos[1])][int(voos[0])] > int(voos[2]):
              grafo[int(voos[1])][int(voos[0])]= int(voos[2])
            else: pass
          else: grafo[int(voos[1])].update({int(voos[0]):int(voos[2])})

def menorCaminho(qtdCidades,grafo):
    menor = float("inf")
    for i in range(qtdCidades): #compara distancia de todas as cidades entre si
        cidades=dijkstra(grafo,i)
        distancia = cidades[max(cidades, key=cidades.get)]#cidades mais distantes entre si
        #entre as mais distantes pega o caminho mais proximo:
        if distancia < menor:
          menor = distancia
    return menor

#main
grafo = {}
entrada = input().split()
qtdCidades, qtdVoos = int(entrada[0]),int(entrada[1])
preencheGrafo(qtdVoos,qtdCidades,grafo)
print(menorCaminho(qtdCidades,grafo))
