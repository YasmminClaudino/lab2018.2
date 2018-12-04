def conta(l,qtd):
    cruza = 0
    y = qtd-2
    constante = qtd-1
    count = qtd-1
    for x in l[::-1]:
        for e in range(count):
            valor = l[y]
            if y < 0:
                break
            if int(x) < int(valor):
                cruza+=1
            y-=1
        constante-=1
        y = constante
    return cruza
qtd = int(input())
valores = input().split()
l = list(valores)
print(conta(l,qtd))
