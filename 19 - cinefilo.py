class Node():
  def __init__(self,dado):
    self.__dado = dado
    self.__filhoEsq = None
    self.__filhoDir = None
    self.__pai = None
  def getDado(self):
    return self.__dado
  def setDado(self,dado):
    self.__dado = dado
  def getPai(self):
    return self.__pai
  def setPai(self,dado):
    self.__pai = dado
  def getEsq(self):
    return self.__filhoEsq
  def setEsq(self, esquerdo):
    self.__filhoEsq = esquerdo
  def getDir(self):
    return self.__filhoDir
  def setDir(self, direito):
    self.__filhoDir = direito
class ABB():
    def __init__(self):
        self.__raiz = None
        self.__string = ""
    def setRaiz(self,novaRaiz):
      self.__raiz = novaRaiz
    def getRaiz(self):
      return self.__raiz
    def zerarString(self):
      self.__string = ""
    def IsEmpty(self):
        return self.__raiz == None
    def insert(self, valor):
      newNode = Node(valor)
      y = None
      x = self.getRaiz()
      while x != None:
        y = x
        if newNode.getDado() < x.getDado():
          x = x.getEsq()
        else:
          x = x.getDir()
      newNode.setPai(y)
      if y == None:
        self.setRaiz(newNode)
      else:
        if newNode.getDado() < y.getDado():
          y.setEsq(newNode)
        else:
          y.setDir(newNode)
    def PreOrder(self, node):
      if node is not None:
        self.__string += str(node.getDado()) + " "
        self.PreOrder(node.getEsq())
        self.PreOrder(node.getDir())
      return self.__string
    def emOrdem(self,node):
      if node is not None:
        self.emOrdem(node.getEsq())
        self.__string += str(node.getDado()) + " "
        self.emOrdem(node.getDir())
      return self.__string
    def posOrdem(self, node):
      if node is not None:
        self.posOrdem(node.getEsq())
        self.posOrdem(node.getDir())
        self.__string += str((node.getDado())) + " "
      return self.__string
    def search(self,x,valor):
      while x != None and valor != x.getDado():
        if valor < x.getDado():
          x = x.getEsq()
        else:
          x = x.getDir()
      return x
    def minimo(self, i):
      if i is not None:
        while i.getEsq() is not None:
          i = i.getEsq()
        return i
    def maximo(self,i):
      if i is not None:
        while i.getDir() is not None:
          i = i.getDir()
        return i
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
    def antecessor(self,x):
      currentNode = self.search(self.getRaiz(),x)
      if currentNode.getEsq() is not None:
        return self.maximo(currentNode.getEsq())
      y = currentNode.getPai()
      while y is not None and currentNode is y.getEsq():
        currentNode = y
        y = y.getPai()
      return y
    def remove(self,dado):
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
        self.setRaiz(x)
      elif y == y.getPai().getEsq():
        y.getPai().setEsq(x)
      else:
        y.getPai().setDir(x)
      if y != dado:
        dado.setDado(y.getDado())
      return y
caso = 1
while True:
  arvore = ABB()
  try:
    qntComandos = int(input())
  except:
    break
  print("Caso %d:" % caso)
  caso +=1
  for x in range(qntComandos):
    listaComandos = [str(x) for x in input().split(" ")]
    if listaComandos[0] == "A":
      arvore.insert(int(listaComandos[1]))
    elif listaComandos[0] == "B":
      deletar = arvore.search(arvore.getRaiz(), int(listaComandos[1]))
      if deletar == None:
        print("0")
      else:
        arvore.remove(deletar)
    elif listaComandos[0] == "C":
      numero = int(listaComandos[1])
      if arvore.search(arvore.getRaiz(),numero) != None and arvore.antecessor(numero) != None:
        maior = arvore.antecessor(numero).getDado()
        print(maior)
      else:
        print(0)
    elif listaComandos[0] == "PRE":
      if arvore.getRaiz() == None:
        print(0)
      else:
        print(arvore.PreOrder(arvore.getRaiz())[:-1])
        arvore.zerarString()
    elif listaComandos[0] == "IN":
      if arvore.getRaiz() == None:
        print(0)
      else:
        print(arvore.emOrdem(arvore.getRaiz())[:-1])
        arvore.zerarString()
    elif listaComandos[0] == "POST":
      if arvore.getRaiz() == None:
        print(0)
      else:
        print(arvore.posOrdem(arvore.getRaiz())[:-1])
        arvore.zerarString()