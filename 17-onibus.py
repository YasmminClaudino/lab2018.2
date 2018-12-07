def procura(lista, atual, destino, caminho = 1, visitados = []):
	if destino in lista[atual]:
		print(caminho)
		return
	visitados.append(atual)
	for i in lista[atual]:
		if i not in visitados:
			if procura(lista, i, destino, caminho+1, visitados):
				return True
	return False


cidades, origem, destino = [int(c) for c in input().split()]
listacidades = [[] for _ in range(cidades)]
for i in range(cidades-1):
	a, b = [int(n) for n in input().split()]
	listacidades[a-1].append(b-1)
	listacidades[b-1].append(a-1)
visitados = []
caminho = 0

procura(listacidades, origem-1, destino-1)
