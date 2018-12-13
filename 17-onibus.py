def buscar(lista, atual, destino, visitados = None,contador = 1):
	if destino in lista[atual]:
		print(contador)
		return
	else:
		for i in lista[atual]:
			if i != visitados:
				buscar(lista, i, destino, atual,contador+1)

c, origem, destino = [int(c) for c in input().split()]
cidades = [[] for x in range(c)]
for i in range(c-1):
	a, b = [int(n) for n in input().split()]
	cidades[a-1].append(b-1)
	cidades[b-1].append(a-1)

buscar(cidades, origem-1, destino-1)
