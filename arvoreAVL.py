class Node():
    def __init__(self, key):
        self._p = None
        self._right = None
        self._key = key
        self._left = None

    def get_key(self):
        return self._key

    def set_key(self, value):
        self._key = value

    def get_right(self):
        return self._right

    def set_right(self, value):
        self._right = value

    def get_left(self):
        return self._left

    def set_left(self, value):
        self._left = value

    def get_p(self):
        return self._p

    def set_p(self, value):
        self._p = value


class AVL():
    def __init__(self):
        self.__empty = Node(None)
        self.__empty.set_left(self.get_empty())
        self.__empty.set_right(self.get_empty())
        self.__empty.set_p(self.get_empty())
        self.__root = self.get_empty()
        self.__string = ""

    def set_string(self, value):
        self.__string = value

    def get_empty(self):
        return self.__empty

    def set_empty(self, valor):
        self.__empty = valor

    def get_root(self):
        return self.__root

    def set_root(self, valor):
        self.__root = valor

    def Altura(self, x):
        if x == self.get_empty():
            return -1
        h1 = self.Altura(x.get_left())
        h2 = self.Altura(x.get_right())
        return (1 + max(h1, h2))

    def Inorder(self, x):
        if x != self.get_empty():
            self.Inorder(x.get_left())
            self.__string += str(x.get_key()) + " "
            self.Inorder(x.get_right())
        return self.__string[:-1]

    def Preorder(self, x):
        if x != self.get_empty():
            self.__string += str(x.get_key()) + " "
            self.Preorder(x.get_left())
            self.Preorder(x.get_right())
        return self.__string[:-1]

    def Postorder(self, x):
        if x != self.get_empty():
            self.Postorder(x.get_left())
            self.Postorder(x.get_right())
            self.__string += str((x.get_key())) + " "
        return self.__string[:-1]

    def Search(self, x, k):
        while x != self.get_empty() and k != x.get_key():
            if k < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
        return x

    def Minimo(self, x):
        while x.get_left() != self.get_empty():
            x = x.get_left()
        return x

    def Maximo(self, x):
        while x.get_right() != self.get_empty():
            x = x.get_right()
        return x

    def Sucessor(self, x):
        if x.get_right() != self.get_empty():
            return self.Minimo(x.get_right())
        else:
            y = x.get_p()
            while y != self.get_empty() and x == y.get_right():
                x = y
                y = y.get_p()
            return y

    def Predecessor(self, x):
        currentNode = self.Search(self.get_root(), x)
        if currentNode.get_left() is not None:
            return self.Maximo(currentNode.get_left())
        y = currentNode.get_p()
        while y is not None and currentNode is y.get_left():
            currentNode = y
            y = y.get_p()
        return y

    def Verify(self, no):
        return self.Altura(no.get_left()) - self.Altura(no.get_right())

    def Balance(self, nodo):
        while nodo.get_p() != self.get_empty():
            if self.Verify(nodo.get_p()) == 2 and self.Verify(nodo) == 1:
                self.Right_Rotate(nodo.get_p())
            if self.Verify(nodo.get_p()) == -2 and self.Verify(nodo) == -1:
                self.Left_Rotate(nodo.get_p())
            if self.Verify(nodo.get_p()) == 2 and self.Verify(nodo) == -1:
                self.Left_Rotate(nodo)
                self.Right_Rotate(nodo.get_p().get_p())
            if self.Verify(nodo.get_p()) == -2 and self.Verify(nodo) == 1:
                self.Right_Rotate(nodo)
                self.Left_Rotate(nodo.get_p().get_p())
            nodo = nodo.get_p()

    def Left_Rotate(self, x):
        y = x.get_right()
        x.set_right(y.get_left())
        if y.get_left() != self.get_empty():
            y.get_left().set_p(x)
        y.set_p(x.get_p())
        if x.get_p() == self.get_empty():
            y.get_left().set_p(x)
        y.set_p(x.get_p())
        if x.get_p() == self.get_empty():
            self.set_root(y)
        elif x == x.get_p().get_left():
            x.get_p().set_left(y)
        else:
            x.get_p().set_right(y)
        y.set_left(x)
        x.set_p(y)

    def Right_Rotate(self, x):
        y = x.get_left()
        x.set_left(y.get_right())
        y.get_right().set_p(x)
        y.set_p(x.get_p())
        if x.get_p() == self.get_empty():
            y.get_right().set_p(x)
        y.set_p(x.get_p())
        if x.get_p() == self.get_empty():
            self.set_root(y)
        elif x == x.get_p().get_right():
            x.get_p().set_right(y)
        else:
            x.get_p().set_left(y)
        y.set_right(x)
        x.set_p(y)

    def Insert(self, dado):
        novo = Node(dado)
        y = self.get_empty()
        x = self.get_root()
        while x != self.get_empty():
            y = x
            if novo.get_key() < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
        novo.set_p(y)
        if y == self.get_empty():
            self.set_root(novo)
        elif novo.get_key() < y.get_key():
            y.set_left(novo)
        else:
            y.set_right(novo)
        novo.set_right(self.get_empty())
        novo.set_left(self.get_empty())
        self.Balance(novo)

    def Delete(self, z):
        z = self.Search(self.get_root(), z)
        if z.get_left() == self.get_empty() or z.get_right() == self.get_empty():
            y = z
        else:
            y = self.Sucessor(z)
        if y.get_left() != self.get_empty():
            x = y.get_left()
        else:
            x = y.get_right()
        if x != self.get_empty():
            x.set_p(y.get_p())
        if y.get_p() == self.get_empty():
            self.set_root(x)
        elif y == y.get_p().get_left():
            y.get_p().set_left(x)
        else:
            y.get_p().set_right(x)
        if y != z:
            z.set_key(y.get_key())
        return y

    def Nivel(self, nodo):
        if nodo == self.get_empty():
            return -1
        else:
            x = nodo
            nivel = 1
            while x != self.get_root():
                x = x.get_p()
                nivel += 1
        return nivel

arvore = AVL()
l = [2,4,1,3,6]
for x in l:
    arvore.Insert(x)
arvore.Predecessor(arvore.get_root())