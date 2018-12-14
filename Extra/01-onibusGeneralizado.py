# infinito:
inf = float("inf")
# dijkstra
def dijkstra(grafo, source):
    # variaveis
    distancia = {}
    no_anterior = {}
    peso_do_no = {}
    q = {}
    # atribui distancias e de onde veio:
    for v in grafo:
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

grafo={}
cidades = input().split(" ")
# constrói voos no grafo:
for i in range(int(cidades[1])):
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
#print(grafo)
#print(dijkstra(grafo,0))
menor = inf
for i in range(int(cidades[0])): #compara distancia de todas as cidades entre si
    cidades=dijkstra(grafo,i)
    distancia = cidades[max(cidades, key=cidades.get)]#cidades mais distantes entre si
    #entre as mais distantes pega o caminho mais proximo:
    if distancia < menor:
      menor = distancia
print(menor)


def menor(dist):
    menor = float("inf")
    for x in dist:
        if x < menor:
            menor = x
    return menor


distancia, q, dist = [], [],[]
qtd, origem, destino = [int(qtd) for qtd in input().split()]
grafo = [[] for x in range(qtd)]
while True:
    a, b, peso = [int(n) for n in input().split()]
    if a == b == peso == 0:
        break
    grafo[a - 1].append(b - 1)
    grafo[b - 1].append(a - 1)
    distancia.append(peso)

dijkstra(grafo, distancia, q)
print(menor(dist))