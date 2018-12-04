#ordena
def partition(l, p, r):
    pivot = l[r]
    i = p-1
    j = r

    done = False
    while not done:

        while not done:
            i = i+1

            if i == j:
                done = True
                break

            if l[i] < pivot:
                l[j] = l[i]
                break

        while not done:
            j = j-1

            if j == i:
                done = True
                break

            if l[j] > pivot:
                l[i] = l[j]
                break

    l[j] = pivot
    return j


def quicksort(l, p, r):
    if p < r:
        q = partition(l, p, r)
        quicksort(l, p, q-1)
        quicksort(l, q+1, r)
    else:
        return
def organiza(lista):
    for x in range(len(lista)):
        for y in range(len(lista)):
            if lista[x][1] == lista[y][1]:
                if lista[x][2] < lista[y][2]:
                    lista[x],lista[y] = lista[y],lista[x]
p = 0
def planos(nome,plano, urgencia, l):
    if plano == "premium":  plano = 10
    elif plano == "diamante": plano = 9
    elif plano == "ouro": plano = 8
    elif plano == "prata":  plano = 7
    elif plano == "bronze":  plano = 6
    elif plano == "resto": plano = 5

    l.append((plano, (urgencia),(nome)))
    return l
qtd = int(input())
lista = []
for x in range(qtd):
    paciente = input().split()
    nome,plano,urgencia = paciente[0],paciente[1],int(paciente[2])
    planos(nome, plano, urgencia,lista)
r = qtd-1
quicksort(lista,p,r)
organiza(lista)

for x in range(qtd):
    print(lista[x][2])

