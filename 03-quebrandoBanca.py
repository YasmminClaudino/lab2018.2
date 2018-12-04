while True:
    try:
        a, b = [int(a) for a in input().split()]
        entrada = input()
        saldo = [int(s) for s in entrada]
        primeiro = saldo[0]
        contador = 0
        j = 1
        i = 0
        tamanho = len(saldo)
        while tamanho > (a-b):
            if i < a-1:
                primeiro = saldo[i]
            if j < a-1:
                segundo = saldo[j]
            if primeiro>=segundo:
                saldo.remove(segundo)
                j+=1
            else:
                saldo.remove(primeiro)
            tamanho-=1
        print(''.join(map(str, saldo)))
    except:
        break
