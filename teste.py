"""
Juvenal se perdeu.
Aluno: Bruno Olimpio dos Santos
"""

class Node():
    u"""Unidade básica para funcionamento da Árvore Binária."""

    def __init__(self, key):
        u"""Classe Node é iniciada com argumentos key e data.
        Argumentos:
            key  - identificador de um objeto Node. Tipo - Inteiro.
            data - informação armazenada pelo objeto Node.
        Atributos:
            left   - filho esquerdo
            right  - filho direito
            parent - nó pai
        """
        self.key = key
        self.data = None
        self.left = None
        self.right = None
        self.parent = None

    def getKey(self):
        """Retorna atributo [key]."""
        return self.key

    def getData(self):
        u"""Retorna conteúdo armazenado."""
        return self.data

    def getLeft(self):
        """Retorna filho esquerdo."""
        return self.left

    def getRight(self):
        """Retorna filho direito."""
        return self.right

    def getParent(self):
        u"""Retorna nó pai."""
        return self.parent

    def setKey(self, key):
        """Define chave de acesso."""
        self.key = key

    def setData(self, data):
        u"""Define conteúdo armazenado."""
        self.data = data

    def setLeft(self, left):
        """Define filho esquerdo."""
        self.left = left

    def setRight(self, right):
        """Define filho direito."""
        self.right = right

    def setParent(self, parent):
        u"""Define nó pai."""
        self.parent = parent

    def __repr__(self):
        """Define retorno da função [print]"""
        return self.getKey()


class Tree():
    u"""Árvore de Busca Binária."""

    def __init__(self):
        u"""
        Inicia a Árvore com raiz None.
        t = Tree(Node())
        """
        self.root = None

    def setRoot(self, root):
        """Atribui valor para [self.root]."""
        self.root = root

    def minimum(self, x):
        """Retorna a menor chave a partir de um nó [x]."""
        if x is not None:
            while x.getLeft() is not None:
                x = x.getLeft()
            return x.getKey()

    def maximum(self, x):
        """Retorna a maior chave a partir de um nó [x]."""
        if x is not None:
            while x.getRight() is not None:
                x = x.getRight()
            return x.getKey()

    def successor(self, x):
        """Menor key maior que x.key."""
        if x is not None:
            if x.getRight() is not None:
                return self.minimum(x.getRight())
            else:
                father = x.getParent()
                while father is not None and x is father.getRight():
                    x = father
                    father = x.getParent()
        return father

    def antecessor(self, x):
        """Maior key menor que x.key."""
        if x is not None:
            if x.getLeft() is not None:
                return self.maximum(x.getLeft())
            else:
                father = x.getParent()
                while (father is not None) and (x is father.getLeft()):
                    x = father
                    father = x.getParent()
        return father

    def insert(self, z):
        u"""Insere um objeto Node na árvore."""
        if self.isEmpty():
            self.setRoot(z)
        else:
            y = None
            x = self.root
            while x is not None:
                y = x
                if z.getKey() < x.getKey():
                    x = x.getLeft()
                else:
                    x = x.getRight()
            z.setParent(y)
            if y is None:
                self.root = z
            elif z.getKey() < y.getKey():
                y.setLeft(z)
            else:
                y.setRight(z)

    def delete(self, z):
        if (z.getLeft() is None) or (z.getRight() is None):
            y = z
        else:
            y = z.successor()
        if y.getLeft() is not None:
            x = y.getLeft()
        else:
            x = y.getRight()
        if x is not None:
            x.setParent(y.getParent())
        if y.getParent() is None:
            self.root = x
        else:
            if y == y.getParent().getLeft():
                y.getParent().setLeft(x)
            else:
                y.getParent().setRight(x)

        if y != z:
            z.setKey(y.getKey())
        # print(y.getKey())

    def preOrderTreeWalk(self, x):
        if x is not None:
            print(x.getKey(), end =' ')
            self.preOrderTreeWalk(x.getLeft())
            self.preOrderTreeWalk(x.getRight())

    def inOrderTreeWalk(self, x):
        if x is not None:
            self.inOrderTreeWalk(x.getLeft())
            print(x.getKey(), end =' ')
            self.inOrderTreeWalk(x.getRight())

    def postOrderTreeWalk(self, x):
        if x is not None:
            self.postOrderTreeWalk(x.getLeft())
            self.postOrderTreeWalk(x.getRight())
            print(x.getKey(), end =' ')

    def search(self, k):
        x = self.root
        while x is not None and k != x.getKey():
            if k < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        return x

    def isEmpty(self):
        if self.root is None:
            return True

saidas =[]
comandos = []
while True:
    comando = input()
    if comando == '':
        break
    else:
        comandos.append(comando)

print('\n')
caso = 0
for i in range(len(comandos)):
    comando = comandos[i].split(' ')
    if comando[0].isdigit():
        caso +=1
        quantidade = int(comando[0])
        print('Caso %d:' % caso)
        arvore = Tree()


        for j in comandos[i+1:(i+quantidade)+1]:
            if j[0] == 'A':
                inserir = int(j[2])
                arvore.insert(Node(inserir))
            elif j[0] == 'B':
                alvo = arvore.search(int(j[2]))
                arvore.delete(alvo)
            elif j[0] == 'C':
                alvo = arvore.search(int(j[2]))
                if arvore.isEmpty():
                    print(0)
                if alvo.getKey() == arvore.minimum(alvo):
                    print(0)
                else:
                    alvo = arvore.search(int(j[2]))
                    print(arvore.antecessor(alvo))
            elif j == 'PRE':
                if arvore.isEmpty():
                    print(0)
                else:
                    arvore.preOrderTreeWalk(arvore.root)
                    print('\n')
            elif j == 'IN':
                if arvore.isEmpty():
                    print(0)
                else:
                    arvore.inOrderTreeWalk(arvore.root)
                    print('\n')
            elif j == 'POST':
                if arvore.isEmpty():
                    print(0)
                else:
                    arvore.postOrderTreeWalk(arvore.root)
                    print('\n')