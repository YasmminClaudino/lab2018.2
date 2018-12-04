def achaLetra(alfa, palavra,decifra,alfabetoC):
    index = alfa.find(palavra)
    formaPalavra(index,alfabetoC)
def formaPalavra(index,alfabetoC):
    global decifra
    novaLetra = alfabetoC[index]
    decifra+=novaLetra
    return decifra

alfa = "abcdefghijklmnopqrstuvwxyz"
alfabetoC = input().lower()
palavra = input().lower()
decifra = ""
for x in range(len(palavra)):
    achaLetra(alfa,palavra[x],decifra,alfabetoC)
print(decifra)