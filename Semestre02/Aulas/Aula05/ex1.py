import os
os.system("cls")

# Exercicio:
# Crie uma função que passe uma frase por parâmetro e substitua todas as vogais por ponto de interrogação (?), retornando a frase modificada

def tiraVogais(s: str) -> str:
    resultado = ""
    for elem in s:
        if elem in "aeiouAEIOU":
            resultado += "?"
        else:
            resultado += elem
    return resultado

frase = "Gustavo Moretim Canzi"
print(tiraVogais(frase))

# ex professor

def troca_vogais(f: str) -> str:
    nf = list()
    vogais = "AEIOU"
    for i in range(len(f)):
        if f[i].upper() in vogais:
            nf.append('?')
        else:
            nf.append(f[i])
    return nf

frase2 = "Edson de Oliveira"
print(frase2)