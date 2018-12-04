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

            if l[i] > pivot:
                l[j] = l[i]
                break

        while not done:
            j = j-1

            if j == i:
                done = True
                break

            if l[j] < pivot:
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

#main


def compara(c1,c2):
    i = 0
    while True:
        t1 = c1[i]
        if i < len(c2):
            t2 = c2[i]
        else:
            return c1[i]
        s = t1 - int(t2)
        if s != 0:
            return c1[i]
        i+=1

qtdPecas = int(input())
conjunto1, conjunto2 = [],[]

for valores in range(1,qtdPecas+1):
    conjunto1.append(valores)

pecasJuvenal = input().split()
for v in pecasJuvenal:
    conjunto2.append(int(v))

r = len(conjunto2)-1
quicksort(conjunto2,p,r)
print(compara(conjunto1,conjunto2))







