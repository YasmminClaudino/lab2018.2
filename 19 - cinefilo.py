class No():
    def __init__(self, chave):
        self._pai = None
        self._dir = None
        self._chave = chave
        self._esq = None

    def getChave(self):
        return self._chave
    def setChave(self, value):
        self._chave = value
    def getDir(self):
        return self._dir
    def setDir(self, value):
        self._dir = value
    def getEsq(self):
        return self._esq
    def setEsq(self, value):
        self._esq = value
    def getPai(self):
        return self._pai
    def setPai(self, value):
        self._pai = value

class arvoreAVL():
    def __init__(self):
        self.__vazio = No(None)
        self.__vazio.setEsq(self.getVazio())
        self.__vazio.setDir(self.getVazio())
        self.__vazio.setPai(self.getVazio())
        self.__raiz = self.getVazio()
        self.__string = ""

    def setString(self, value):
        self.__string = value

    def getVazio(self):
        return self.__vazio

    def setVazio(self, valor):
        self.__vazio = valor

    def getRaiz(self):
        return self.__raiz

    def setRaiz(self, valor):
        self.__raiz = valor

    def inserirElemento(self, dado):
        novo = No(dado)
        y = self.getVazio()
        x = self.getRaiz()
        while x != self.getVazio():
            y = x
            if novo.getChave() < x.getChave():
                x = x.getEsq()
            else:
                x = x.getDir()
        novo.setPai(y)
        if y == self.getVazio():
            self.setRaiz(novo)
        elif novo.getChave() < y.getChave():
            y.setEsq(novo)
        else:
            y.setDir(novo)
        novo.setDir(self.getVazio())
        novo.setEsq(self.getVazio())
        self.balanceamento(novo)

    def buscar(self, x, k):
        while x != self.getVazio() and k != x.getChave():
            if k < x.getChave():
                x = x.getEsq()
            else:
                x = x.getDir()
        return x

    def minimo(self, x):
        while x.getEsq() != self.getVazio():
            x = x.getEsq()
        return x

    def maximo(self, x):
        while x.getDir() != self.getVazio():
            x = x.getDir()
        return x

    def sucessor(self, x):
        if x.getDir() != self.getVazio():
            return self.minimo(x.getDir())
        else:
            y = x.getPai()
            while y != self.getVazio() and x == y.getDir():
                x = y
                y = y.getPai()
            return y

    def verifica(self, no):
        return self.altura(no.getEsq()) - self.altura(no.getDir())

    def altura(self, x):
        if x == self.getVazio():
            return -1
        h1 = self.altura(x.getEsq())
        h2 = self.altura(x.getDir())
        return (1 + max(h1, h2))

    def balanceamento(self, nodo):
        while nodo.getPai() != self.getVazio():
            if self.verifica(nodo.getPai()) == 2 and self.verifica(nodo) == 1:
                self.rotacaoSDireita(nodo.getPai())
            if self.verifica(nodo.getPai()) == -2 and self.verifica(nodo) == -1:
                self.rotacaoSEsquerda(nodo.getPai())
            if self.verifica(nodo.getPai()) == 2 and self.verifica(nodo) == -1:
                self.rotacaoSEsquerda(nodo)
                self.rotacaoSDireita(nodo.getPai().getPai())
            if self.verifica(nodo.getPai()) == -2 and self.verifica(nodo) == 1:
                self.rotacaoSDireita(nodo)
                self.rotacaoSEsquerda(nodo.getPai().getPai())
            nodo = nodo.getPai()

    def rotacaoSEsquerda(self, x):
        y = x.getDir()
        x.setDir(y.getEsq())
        if y.getEsq() != self.getVazio():
            y.getEsq().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == self.getVazio():
            y.getEsq().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == self.getVazio():
            self.setRaiz(y)
        elif x == x.getPai().getEsq():
            x.getPai().setEsq(y)
        else:
            x.getPai().setDir(y)
        y.setEsq(x)
        x.setPai(y)

    def rotacaoSDireita(self, x):
        y = x.getEsq()
        x.setEsq(y.getDir())
        y.getDir().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == self.getVazio():
            y.getDir().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == self.getVazio():
            self.setRaiz(y)
        elif x == x.getPai().getDir():
            x.getPai().setDir(y)
        else:
            x.getPai2().setEsq(y)
        y.setDir(x)
        x.setPai(y)

    def nivel(self, nodo):
        if nodo == self.getVazio():
            return -1
        else:
            x = nodo
            nivel = 1
            while x != self.getRaiz():
                x = x.getPai()
                nivel += 1
        return nivel

    def removeElemento(self, z):
        z = self.buscar(self.getRaiz(), z)
        if z.getEsq() == self.getVazio() or z.getDir() == self.getVazio():
            y = z
        else:
            y = self.sucessor(z)
        if y.getEsq() != self.getVazio():
            x = y.getEsq()
        else:
            x = y.getDir()
        if x != self.getVazio():
            x.setPai(y.getPai())
        if y.getPai() == self.getVazio():
            self.setRaiz(x)
        elif y == y.getPai().getEsq():
            y.getPai().setEsq(x)
        else:
            y.getPai().setDir(x)
        if y != z:
            z.setChave(y.getChave())
        return y


def comandos(qtd):
    guarda = []
    for x in range(qtd):
        bancoDados = arvoreAVL()
        while True:
            instrucao = input()
            if instrucao[0] == "I":
                bancoDados.inserirElemento(int(instrucao[1:]))
            elif instrucao[0] == "N":
                print(bancoDados.nivel(bancoDados.buscar(bancoDados.getRaiz(), int(instrucao[1:]))))
            elif instrucao[0] == "L":
                filmes = instrucao.split(" ")
                for x in range(int(filmes[1]), int(filmes[2]) + 1):
                    if bancoDados.buscar(bancoDados.getRaiz(), x).getChave() is not None:
                        guarda.append(x)
                print(" ".join(map(str,guarda)))
            else:
                break
        if x != qtd - 1:
            print("")

qtd = int(input())
comandos(qtd)
