#Notação Polonesa \\Henrique Cesar

class Nor:

    def __init__(self, dados):
        self.dados = dados
        self.proximoNor = None

    def inserirProximo(self, novoNor):
        self.proximoNor = novoNor

    def obterDados(self):
        return self.dados

    def obterProx(self):
        return self.proximoNor


class Pilha:

    def __init__(self):
        self.topo = None
        self.base = None

    def verificarSeVazia(self):
        return self.base is None

    def zerarPilha(self):
    	self.topo = self.base = None

    def empilhar(self, dados):
        novoNor = Nor(dados)
        if self.verificarSeVazia():
            self.base = self.topo = novoNor
        else:
            novoNor.inserirProximo(self.topo)
            self.topo = novoNor

    def desempilhar(self):
        pop = self.topo.obterDados()
        if self.topo == self.base:
            self.topo = self.base = None
        else:
            self.topo = self.topo.obterProx()
        return pop


def calcula(operador, operando1, operando2):
    if operador == "+":
        return operando1 + operando2
    if operador == "-":
        return operando1 - operando2
    if operador == "*":
        return operando1 * operando2
    else:
        return int(operando1 / operando2)


operadores = ["+", "-", "*", "/"]
pilha = Pilha()
somatempo = 0
while True:
    try:
        operacao = input().split()
        for x in range(len(operacao)-1,-1,-1):
            if operacao[x] in operadores:
                operando1 = int(pilha.desempilhar())
                operando2 = int(pilha.desempilhar())
                resultado = calcula(operacao[x], operando1, operando2)
                pilha.empilhar(resultado)
            else:
                pilha.empilhar(int(operacao[x]))
        print(pilha.topo.obterDados())
        pilha.zerarPilha()
    except:
        break