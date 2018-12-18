inf = float("inf")
def dijkstra(grafo, source):
    distancia = {}
    no_anterior = {}
    peso_do_no = {}
    q = {}
    # atribui distancias e de onde veio:
    for vertice in grafo.items():
      v=vertice[0]
      distancia[v] = inf
      no_anterior[v] = None
    distancia[source] = 0
    q = distancia
    while len(q) is not 0:
        u = min(q, key=q.get) #menor da queue
        peso_do_no[u] = q.pop(u)
        for v in grafo[u]: #para cada vertice adjacente nao visitado:
          temp_distancia = peso_do_no[u] + grafo[u][v]
          if v in q:
              #relaxa:
              if q[v] > peso_do_no[u] + grafo[u][v]:
                q[v] = temp_distancia
                no_anterior[v] = u
    return peso_do_no

grafo = {0: {1: 2, 2: 4}, 1: {3: 1, 0: 2}, 2: {0: 4, 3: 5, 3: 2}, 3: {1: 1, 2: 5, 2: 2}}

print(dijkstra(grafo,0))
