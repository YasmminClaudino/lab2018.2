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

fila = Fila()

l = [1,2,3,4,5]

for x in l:
    fila.insereElemento(x)
    print(fila)

for x in range(len(l)):
    fila.removeElemento()
    print(fila)