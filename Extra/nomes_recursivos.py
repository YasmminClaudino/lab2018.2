def substring(nome,i,j):
    tamanho = len(nome)
    n = nome[i:j]
    if j<= tamanho:
        j+=1
        print(n)
        substring(nome,i,j)
    else:
        print()
        i+=1
        if i <= tamanho-1:
            j = i + 1
            substring(nome,i,j)


nome = input()
i,j = 0, 1
substring(nome,i,j)