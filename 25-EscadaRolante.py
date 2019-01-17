def escada(qtdPessoas, pessoa1, total=0):
    for x in range(qtdPessoas-1):
        tempo = int(input())
        e = tempo - pessoa1
        if e >=10:
            total+=10
        else:
            total+=e
        pessoa1 = tempo
    return total

qtdPessoas = int(input())
pessoa1 = int(input())
t = escada(qtdPessoas,pessoa1)
print(t+10)
