#ordena
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
            if pivot != tuple:
                if l[i] < pivot:
                   l[j] = l[i]
            if l[i] < pivot:
                l[j] = l[i]
                break

        while not done:
            j = j-1

            if j == i:
                done = True
                break
            if pivot != tuple:
                if l[j] > pivot:
                    l[i] = l[j]
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
p = 0

def organiza(dic):
    for x in range(len(dic)+1):
        for y in range(len(dic)+1):
                if dic[x] < dic[y]:
                    lista[x] = lista[y]
                    lista[y] = lista[x]

entrada = input().split()
qtdP, times = int(entrada[0]), int(entrada[1])
lista = []
dicTimes = {}
for x in range(qtdP):
    pessoas = input().split()
    nome, ponto = pessoas[0], int(pessoas[1])
    lista.append((ponto,nome))
r = qtdP-1
quicksort(lista,p,r)


for dic in range(times):
    dicTimes[dic] = []


id = 0
for ele in lista:
    dicTimes[id].append(ele[1])
    id+=1
    if id == times:
        id = 0


for x in range(times):
   organiza(dicTimes[x])

for x in range(times):
    for i in range(1):
        print("Time %d" %(x+1))
        for y in (dicTimes[x]):
            print(y)
        print()