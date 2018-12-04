class No():
    def __init__(self, chave, dado):
        self.__dado = dado
        self.__chave = chave
        self.__pai = None
        self.__esq = None
        self.__dir = None

    def getDado(self):
        return self.__dado
    def setDado(self, dado):
        self.__dado = dado
    def getChave(self):
        return self.__chave
    def setChave(self, chave):
        self.__chave = chave
    def getPai(self):
        return self.__pai
    def setPai(self, pai):
        self.__pai = pai
    def getEsq(self):
        return self.__esq
    def setEsq(self, esq):
        self.__esq = esq
    def getDir(self):
        return self.__dir
    def setDir(self, direito):
        self.__dir = direito

class ArvoreBinaria():
    def __init__(self):
        self._raiz = None
    def getRaiz(self):
        return self._raiz
    def insereElemento(self, chave, dado=None):
        novoNo = No(chave,dado)
        if self._raiz is None:
            self._raiz = novoNo
        else:
            noAtual = self._raiz
            while noAtual is not None:
                if chave < noAtual.getChave():
                    if noAtual.getEsq() is not None:
                        noAtual = noAtual.getEsq()
                    else:
                        noAtual.setEsq(novoNo)
                        break
                else:
                    if noAtual.getDir() is not None:
                        noAtual = noAtual.getDir()
                    else:
                        noAtual.setDir(novoNo)
                        novoNo.setPai(noAtual)
                        break
            novoNo.setPai(noAtual)

    def estaVazia(self):
        return self._raiz is None
    def minimo(self, i):
        if i != None:
            while i.getEsq() != None:
                i = i.getEsq()
            return i

    def maximo(self, i):
        if i != None:
            while i.getDir() != None:
                i = i.getDir()
            return i

    def preOrdem(self, no):
        if no is not None:
          print(no.getChave(),end=" ")
          self.preOrdem(no.getEsq())
          self.preOrdem(no.getDir())


    def emOrdem(self, no):
        if no is not None:
          self.emOrdem(no.getEsq())
          print(no.getChave(),end=" ")
          self.emOrdem(no.getDir())

    def posOrdem(self,no):
        if no is not None:
          self.posOrdem(no.getEsq())
          self.posOrdem(no.getDir())
          print(no.getChave(),end=" ")

    def buscar(self, k):
        i = self._raiz
        while i is not None:
          if i.getChave() == k:
            return i #vai retornar o no completo / chave e dado
          else:
            if k <i.getChave():
              i = i.getEsq()
            else:
              i = i.getDir()
        return i
    def antecessor(self,x):
        if x is not None:
            if x.getEsq() is not None:
                s = self.minimo(x.getEsq())
                return self.minimo(x.getEsq())
            else:
                pai = x.getPai()
                while pai is not None and x is pai.getEsq():
                    x = pai
                    pai = x.getPai()
                return pai
    def sucessor(self,x):
        if x is not None:
            if x.getDir() is not None:
                return self.minimo(x.getDir())
            else:
                pai = x.getPai()
                while pai is not None and x is pai.getDir():
                    x = pai
                    pai = x.getPai()
                return pai

    def removeElemento(self, dado):
        if dado.getEsq() == None or dado.getDir() == None:
            y = dado
        else:
            y = self.sucessor(dado)
        if y.getEsq() != None:
            x = y.getEsq()
        else:
            x = y.getDir()
        if x is not None:
            x.setPai(y.getPai())
        if y.getPai() == None:
            self._raiz  = x
        elif y == y.getPai().getEsq():
            y.getPai().setEsq(x)
        else:
            y.getPai().setDir(x)
        if y != dado:
            dado.setDado(y.getDado())
        return y

#main
def comandos(qtd,arvore):
    for x in range(qtd):
        entrada = input().split()
        inst = entrada[0]
        if inst == "A":
            arvore.insereElemento(int(entrada[1]))
        elif inst == "B":
            acha = arvore.buscar(int(entrada[1]))
            if acha != None:
                arvore.removeElemento(acha)
            else:
                print(0)
        elif inst == "C":
            acha = arvore.buscar(int(entrada[1]))
            if acha != None:
                ant = arvore.antecessor(acha)
                if ant != None:
                    print(arvore.antecessor(acha).getChave())
                else:
                    print(0)
            else:
                print(0)
        elif inst == "PRE":
            if arvore.estaVazia() is True:
                print(0)
            else:
                arvore.preOrdem(arvore.getRaiz())
                print("")
        elif inst == "IN":
            if arvore.estaVazia() is True:
                print(0)
            else:
                arvore.emOrdem(arvore.getRaiz())
                print("")
        elif inst == "POST":
            if arvore.estaVazia() is True:
                print(0)
            else:
                arvore.posOrdem(arvore.getRaiz())
                print("")
cases = 1
while True:
    try:
        arvore = ArvoreBinaria()
        qtd = int(input())
        print("Caso %d: " %cases)
        comandos(qtd,arvore)
        cases+=1
    except:
        break
