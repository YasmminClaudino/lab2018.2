def buscaPInicial(lista):
    if "N" in lista:
        return "N"
    elif "S" in lista:
        return  "S"
    elif "O" in lista:
        return "O"
    elif "L" in lista:
        return  "L"
    return False
def taNaArena(v, tamanho):
    if 0 <= v < tamanho:
        return True
    return False

def anda(posicao, direcao, tamanhoLinha, tamanhoColuna):
    linha = posicao[0]
    coluna = posicao[1]
    if direcao == "N":
        linha-=1
        if not taNaArena(linha, tamanhoLinha):
            return False

    elif direcao == "S":
        linha+=1
        if not taNaArena(linha, tamanhoLinha):
            return False
    elif direcao == "O":
        coluna-=1
        if not taNaArena(coluna, tamanhoColuna):
            return False
    elif direcao == "L":
        coluna+=1
        if not taNaArena(coluna, tamanhoColuna):
            return False
    d = (linha,coluna)

    return (d)


def rotacionaDireita(direcao):
    if direcao == "N":
        return "L"
    elif direcao == "S":
        return "O"
    elif direcao == "O":
        return "N"
    elif direcao == "L":
        return "S"
def rotacionaEsqueda(direcao):
    if direcao == "N":
        return "O"
    elif direcao == "S":
        return "L"
    elif direcao == "O":
        return "S"
    elif direcao == "L":
        return "N"

#construir mapa
while True:
    linhas, colunas, qtdInst = [int(linhas) for linhas in input().split()]
    if linhas == colunas == qtdInst == 0:
        break
    mapa = []
    posicaoInical = -1
    qtdFigurinhas = 0
    for guarda in range(linhas):
        vMapa = list(input())

        if posicaoInical == -1 and buscaPInicial(vMapa):
            direcao = buscaPInicial(vMapa)
            linha = guarda
            coluna = vMapa.index(direcao)
            posicao = (linha,coluna)
        mapa.append(vMapa)
    instrucoes = input()

    for inst in instrucoes:
        if inst == "E":
            direcao = rotacionaEsqueda(direcao)
        elif inst == "D":
            direcao = rotacionaDireita(direcao)
        else:
            posicaoAtual = anda(posicao,direcao,linhas,colunas)
            if posicaoAtual !=False:
                celula = mapa[posicaoAtual[0]][posicaoAtual[1]]
                if celula =="#":
                    continue
                else:
                    posicao = posicaoAtual
                    if mapa[posicao[0]][posicao[1]] == "*":
                        qtdFigurinhas+=1
                        mapa[posicao[0]][posicao[1]] = "."
    print(qtdFigurinhas)