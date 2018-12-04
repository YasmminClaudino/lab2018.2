def substring(nome,i,j):
    tamanho = len(nome)
    n = nome[i:j]
    if j<= tamanho:
        j+=1
        print(n)
        substring(nome,i,j)
    else:
        print()

nome = input()
for i in range(len(nome)):
    j = i + 1
    substring(nome,i,j)