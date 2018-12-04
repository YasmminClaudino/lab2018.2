def constroeTabuleiro(tabuleiro, qtdL):
    for x in range(qtdL):
        valores = input()
        tabuleiro.append(valores)
    return tabuleiro


#main
tabuleiro = []
valoresMatriz = input().split()
qtdL, qtdC = int(valoresMatriz[0]), int(valoresMatriz[1])
print(constroeTabuleiro(tabuleiro, qtdL))
qtdDisparos = int(input())
disparos(qtdDisparos)
