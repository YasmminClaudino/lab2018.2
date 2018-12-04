def constroeMatriz(lista, qtdL,qtdC):
     for i in range(qtdL):
        for j in range(qtdC):
            valores = list(input())
            lista.append(valores)
        return lista

def descobrePasto(lista,i, j):
    global codigo
    qtdLobos,qtdOvelhas = 0, 0
    celula = lista[i][j]
    if celula == ".":
        lista[i][j] = "vi"
        return
    elif celula == "*" or celula == "#":
        return

    elif celula == "k":
        qtdOvelhas+=1
    elif celula == "v":
        qtdLobos+=1

    lista[i][j] = "*"


    descobrePasto(lista,i-1,j)
    descobrePasto(lista,i,j+1)
    descobrePasto(lista,i+1,j)
    descobrePasto(lista,i,j-1)
    codigo+=1
def calculaAnimais(qtdO,qtdL)
    ovelhas, lobos = 0,0
    if qtdO > qtdLobos:

#main
matriz = []
i, j,codigo = 0, 0,0
qtdOvelhas, qtdLobos = 0, 0
valoresMatriz = input().split()
qtdL, qtdC = int(valoresMatriz[0]), int(valoresMatriz[1])
constroeMatriz(matriz, qtdL,qtdC)
for x in range(qtdL*qtdC):
    descobrePasto(matriz,i,j)
    if j < qtdC-1:
        j+=1
    else:
        j = 0
        i+=1
total = calculaAnimais(pasto, qtdL, qtdC, i, j)
#print("%d %d" %(total[0], total[1]))
print(matriz)