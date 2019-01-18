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
l = [3,2]
r = 1 #tamanho da lista -1
quicksort(l,p,r)
print(l)