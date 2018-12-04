def insere(esquerda,direita,qtd):
    for x in range(qtd):
        entrada = input().split()
        if entrada[1] == "D":
            direita.append(entrada[0])
        elif entrada[1] == "E":
            esquerda.append(entrada[0])
def verifica(esqurda,direita,count):
    for e in direita:
        if e in esquerda:
            count+=1
            esquerda.remove(e)
    return count
#main

qtd = int(input())
esquerda,direita = [],[]
insere(esquerda,direita,qtd)
print(verifica(esquerda,direita,count=0))