def insereGrafo(qtdVoos,grafo):
    for i in range(qtdVoos):
        entrada2 = input().split()
        origem, destino, distancia = int(entrada2[0]),int(entrada2[1]),int(entrada2[2])
        if origem not in grafo: #se a origem n tiver no grafo pra criar uma chave com o dado da origem
            grafo[origem]= {destino:distancia}
        else:
            if destino in grafo[origem]: #se a chave de origem tiver no grafo
                if grafo[origem][destino] > distancia: #se a distancia da origem for > que a atual, a nova distncia será a atual
                    grafo[origem][destino] = distancia
            else:
                grafo[origem].update({destino:distancia}) #atualizar o valor da nova distancia no grafo
        if destino not in grafo: #se o destino não tiver no grago, cria uma chave que recebe o valor da origem e distancia
            grafo[destino]= {origem:distancia}
        else:
            if origem in grafo[destino]: #se já existir, verifica o valor, se a distancia da vertice for maior que a distancia atual, então troca para a nova distancia
                if grafo[destino][origem] > distancia:
                    grafo[destino][origem] = distancia
            else:
                grafo[destino].update({origem:distancia}) #atualiza o valor da nova distancia

def menorElementoQ(q):
    menor = min(q, key=q.get)
    return menor
def dijkstra(grafo, origem,caminho,anterior,dist):
    q = {}
    for vertice in grafo:
      dist[vertice] = float("inf")
      anterior[vertice] = None
    dist[origem] = 0
    q = dist
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
#Verificar o menor caminho entre todas as cidades do grafo
def maiorDistancia(cidades):
    maior = cidades[max(cidades, key=cidades.get)]
    return maior
def menorCaminho(qtdCidades,grafo):
    caminho, anterior, dist = {},{},{}
    menor = float("inf")
    for i in range(qtdCidades):
        cidades = dijkstra(grafo,i,caminho,anterior,dist)
        distancia = maiorDistancia(cidades)
        if distancia < menor:
          menor = distancia
    return menor

#main
grafo = {}
entrada = input().split()
qtdCidades, qtdVoos = int(entrada[0]),int(entrada[1])
insereGrafo(qtdVoos,grafo)
print(menorCaminho(qtdCidades,grafo))
