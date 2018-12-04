nome = input()
tamanho = len(nome)
n = 0
for i in range(tamanho):
    n = i + 1
    for j in range(n,tamanho+1):
        substring = nome[i:j]
        print(substring)
        j+=1
    print()