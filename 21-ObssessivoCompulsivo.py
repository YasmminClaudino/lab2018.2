# dijkstra adaptado:
inf = float("inf")
def Dijkstra(graph,source,end):
  dist={} #distancias
  prev={} #De onde veio
  Q={} #Fila
  #constroi distancias:
  for v in graph.items():
    dist[v[0]]=inf
    Q[v[0]]=inf
    prev[v[0]]=None
  dist[source]=0
  Q[source]=0
  while len(Q) is not 0:
    u= min(Q, key=Q.get) #recebe nó com menor distancia
    distancia_U=dist[u]
    tira_da_fila=Q.pop(u) #Marca como visitado

    for vizinho in graph[u].items():
      #relaxa:
      alt = distancia_U + vizinho[1]
      if alt < dist[vizinho[0]]:
        dist[vizinho[0]]=alt#recebe menor distancia
        prev[vizinho[0]]=u#recebe de onde veio
  return prev

grafo={}
# constói cidades no grafo:
cidades = input().split(" ")
for i in range(1,int(cidades[0])+1):
    grafo[i] = {}
# constrói estradas no grafo:
for i in range(int(cidades[1])):
    estradas = input().split(" ")
    estrada = [int(x) for x in estradas]
    if estrada[1] not in grafo[estrada[0]]:
        grafo[estrada[0]].update({estrada[1]:estrada[2]})
        grafo[estrada[1]].update({estrada[0]:estrada[2]})
    else:
        if grafo[estrada[0]][estrada[1]] > estrada[2]: #estrada com menor distancia prevalece
            grafo[estrada[0]].update({estrada[1]:estrada[2]})
            grafo[estrada[1]].update({estrada[0]:estrada[2]})
print(Dijkstra(grafo,1,int(cidades[0])))