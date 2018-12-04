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

class Pilha():
    def __init__(self):
        self._inicio = None
        self._fim = None

    def __str__(self):
        noAtual = self._inicio
        string = ""
        while noAtual is not None:
            string += str(noAtual.getDado()) + " "
            noAtual = noAtual.getProx()
        return string

    def push(self,dado):
        novoNo = No(dado)
        if self._inicio == None:
            self._inicio = novoNo
            self._fim = novoNo
        else:
            novoNo.setProx(self._inicio)
            self._inicio = novoNo

    def pop(self):
        valorPrimeiroNo = self._inicio.getDado()
        if self._inicio is self._fim:
            self._inicio = None
            self._fim = None
        else:
            self._inicio = self._inicio.getProx()
        return valorPrimeiroNo

    def vazia(self):
        return self._inicio is None
    def limpaPilha(self):
        self._inicio = None
        self._fim = None

l = [1,2,3,4,5]
p = Pilha()
for x in l:
    p.push(x)
    print(p)

for x in range(len(l)):
    p.pop()
    print(p)