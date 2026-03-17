# Crie uma função chamada media_lista(lista) que receba uma lista de números e retorne a média dos valores.
# No programa principal, exiba o resultado da média.

import os
os.system("cls")

def preencherLista(l: list) -> None:
    while True:
        elem = input("Elemento: ")
        if elem != '.':
            l.append(float(elem))
        else:
            break

lista = []
preencherLista(lista)

def mediaLista(l: list) -> float:
    return sum(l) / len(l)

print(f"A média da lista é {mediaLista(lista)}")