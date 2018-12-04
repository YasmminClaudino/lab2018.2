def sucessor(x):
    s = x + 1
    return s

def soma(x,y):
    for i in range(y):
        x = sucessor(x)
    return x

def multiplicador(x,y):
    s = 0
    for i in range(y):
        s = soma(s,x)
    return s

def exponenciacao(expoente, base):
    s = 1
    for i in range(expoente):
        s = multiplicador(s, base)
    return s

expoente = int(input("Expoente: "))
base = int(input("Base: "))
print(exponenciacao(expoente,base))
888a8888