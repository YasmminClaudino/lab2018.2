#funções
def buscar(lista, atual, chegada, contador = 1, listaVisitados = []):
	if chegada in lista[atual]:
		print(contador)
		return
	else:
		listaVisitados.append(atual)
		for j in lista[atual]:
			if j not in listaVisitados:
				if buscar(lista, j, chegada, contador+1, listaVisitados):
					return True
	return False

#main
qtd, cOrigem, cChegada = [int(x) for x in input().split()]
cidades = [[] for x in range(qtd)]
for i in range(qtd-1):
	a, b = [int(y) for y in input().split()]
	cidades[a-1].append(b-1)
	cidades[b-1].append(a-1)
listaVisitados = []
contador = 0

buscar(cidades, cOrigem-1, cChegada-1)