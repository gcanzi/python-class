# fazer um procedimento que exiba na tela o indice e o conteudo de uma lista

import os 
os.system("cls")

def exibeLista1(l: list) -> None:
    for i in range(len(l)):
        print(f"{i} -> {l[i]}")

def exibeLista2(l: list) -> None:
    for ind, elem in enumerate(l):
        print(f"{ind} -> {elem}")

# Principal
lista = [45, 23, "CP4", 56.67]

exibeLista1(lista)
exibeLista2(lista)