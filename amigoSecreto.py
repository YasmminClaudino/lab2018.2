import random
def sorteia(random,nomes):
    pessoa = random.choice(nomes)
    return pessoa


def guardaNome(nomes,qtd):
    for x in range(qtd):
        nome = input("Digite o nome de quem vai participar, incluindo seu nome: ")
        nomes.append(nome)

def amigoSecreto(pessoa,nomes):
    print("Seu inimigo secreto é: %s" %pessoa)
    nomes.remove(pessoa)
    return

nomes = []
qtd = int(input("Digite a quantidade de pessoas que irão participar: "))
guardaNome(nomes,qtd)
while len(nomes) != 0:
    nome = input("Digite seu nome: ")
    pessoa = sorteia(random,nomes)
    if nome != pessoa:
        amigoSecreto(pessoa,nomes)
