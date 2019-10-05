entrada = input().split(' ')
e = int(entrada[0])
del entrada[0]
for i in range(len(entrada)):
    entrada[i] = int(entrada[i])


def quantasVezes(lista, n):
    check = True
    cont = 0
    while check:
        check = False
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                cont += 1
                check = True
    return cont


ordenacao = quantasVezes(entrada, e)
print(ordenacao)
