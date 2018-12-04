class No():
    def __init__(self,dado):
        self.dado = dado
        self.prox = None
    def getDado(self):
        return self.dado
    def getProx(self):
        return self.prox
    def setProx(self,novoNo):
        self.prox = novoNo

class Fila():
    def __init__(self):
        self._inicio = None
        self._fim =  None

    def __str__(self):
        noAtual = self._inicio
        string = ""
        while noAtual is not None:
            string += str(noAtual.getDado()) + " "
            noAtual = noAtual.getProx()
        return string

    def insereElemento(self,dado):
        novoNo = No(dado)
        if self._inicio == None:
            self._inicio = novoNo
            self._fim = novoNo
        else:
            self._fim.setProx(novoNo)
            self._fim =  novoNo

    def removeElemento(self):
        valorPrimeiroNo = self._inicio.getDado()
        if self._inicio is self._fim:
            self._inicio = None
            self._fim = None
        else:
            self._inicio = self._inicio.getProx()
        return valorPrimeiroNo

    def primeiroElemento(self):
        return self._inicio.getDado()
    def zeraFila(self):
        self._inicio = self._fim = None


#main
filaDeckMesa = Fila()
qtdFestas = int(input())
jogadores = {}

for festas in range(qtdFestas):
    chave = 1
    contador = 1
    achou = False
    deckmesa = input().split()
    for x in deckmesa:
        filaDeckMesa.insereElemento(int(x))
    while True:
        convidados = input().split()
        cValores = [int(c) for c in convidados]
        if cValores[0] == -1:
            break
        jogadores[chave] = cValores
        chave+=1
    while True:
        if contador > 1000:
            print("0")
            break
        elif achou is True:
            break
        topDeck = filaDeckMesa.primeiroElemento()
        for pega in range(len(jogadores)):
            cartas = jogadores[pega+1]
            if len(cartas) == 0:
                achou = True
                print(pega+1)
                break
            if len(cartas) > 0:
                top = cartas[0]
                if top == topDeck:
                    cartas.remove(top)
                else:
                    cartas.append(top)
                    cartas.remove(top)
        filaDeckMesa.removeElemento()
        filaDeckMesa.insereElemento(topDeck)
        contador+=1
    jogadores.clear()
    filaDeckMesa.zeraFila()