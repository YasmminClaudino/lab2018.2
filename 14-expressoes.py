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

def insere(p,expressoes):
    for e in expressoes:
        if e == "{" or e == "[" or e == "(":
            p.push(e)
        else:
            if p.vazia():
                print("N")
                break
            elif e == "}":
                if p.pop() != "{":
                    print("N")
                    break
            elif e == "]":
                if p.pop() != "[":
                    print("N")
                    break
            elif e == ")":
                if p.pop() != "(":
                    print("N")
                    break
    else:
        if p.vazia():
            print("S")
        else:
            print("N")

p = Pilha()
qtd = int(input())
for x in range(qtd):
    expressoes = input()
    insere(p,expressoes)
    p.limpaPilha() #limpa a pilha no final de cada expressao testada
