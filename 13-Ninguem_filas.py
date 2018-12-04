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

class ListaEncadeada():
    def __init__(self):
        self._inicio = None
    def inserirNoInicio(self,dado):
        novoNo = No(dado)
        novoNo.prox = self._inicio
        self._inicio = novoNo
    def buscaElemento(self,dado):
        i = self._inicio
        ant = None
        while i != None:
            if i.getDado() == dado:
                return (i,ant)
            ant = i
            i = i.getProx()
        return (i,ant)

    def removeElemento(self,dado):
        no,ant = self.buscaElemento(dado)
        if no !=None:
            if ant != None:
                ant.setProx(no.getProx())
            else:
                self._inicio = no.getProx()
    def imprimeElementos(self,m,n):
        no = self._inicio
        valores = []
        for x in range(m-n):
            valores.insert(0,no.getDado())
            no = no.getProx()
        return valores


#main
encadeada = ListaEncadeada()

qtdPessoas = int(input())
entraFila = input().split()
qtdSaiFila = int(input())
saiFila = input().split()

if (qtdPessoas and qtdSaiFila >= 1) and (qtdSaiFila < qtdPessoas):
    for x in entraFila:
        valorEntrada = int(x)
        encadeada.inserirNoInicio(valorEntrada)

    for y in saiFila:
        saiValor = int(y)
        encadeada.removeElemento(saiValor)
    imprime = encadeada.imprimeElementos(qtdPessoas,qtdSaiFila)
    print(' '.join(map(str, imprime)))