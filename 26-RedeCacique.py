def quicksort(l, p, r):
    if p < r:
        q = partition(l, p, r)
        quicksort(l,p,q-1)
        quicksort(l,q+1,r)

def partition(l, p, r):
    pivot = l[r]
    i = p-1
    for j in range(p,(r-1)+1):
        if l[j] <=  pivot:
            i+=1
            l[i], l[j] = l[j], l[i]
    l[i + 1], l[r] = l[r], l[i + 1]
    return (i+1)
p = 0

def kruskal(grafo, vertices):
    q = {}
    arestas = [set(i) for i in vertices]
    elementos = sorted(grafo, key=grafo.get)
    for x in elementos:
        a = busca(arestas, x[0])
        b = busca(arestas, x[1])
        if a != b:
            conjuntoB = arestas.pop(busca(arestas, x[0]))
            conjuntoA = arestas.pop(busca(arestas, x[1]))
            arestas.append(conjuntoA.union(conjuntoB))
            q[(x[0], x[1])] = grafo[(x[0], x[1])]
    return q

def busca(caminhos, v,contador = 0):
    vertice = None
    for caminho in caminhos:
        if v in caminho:
            vertice = contador
        contador += 1
    return vertice

def percorre(grafo, vertices):
    caminhos = {}
    q = kruskal(grafo, vertices)
    ordenar = [sorted(i) for i in q]
    r = len(ordenar)-1
    quicksort(ordenar,p,r)
    #print("quick", ordenar)
    t = len(ordenar)
    print(n-t)

#main
contador = 1
while True:
    grafo = {}
    n, redes = [int(n) for n in input().split()]
    if n == redes == 0:
        break
    if contador != 1:
        print(' ')
    print('Teste %d' % contador)
    vertices = set()
    for i in range(redes):
        entrada = input().split()
        a, b = entrada[0],entrada[1]
        impacto = 1
        grafo[(a, b)] = impacto
        vertices.update(a, b)
    i+=1
    percorre(grafo, vertices)
    contador += 1