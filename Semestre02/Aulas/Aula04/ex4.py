# Crie um procedimento chamado preencher_lista(lista) que passe uma lista por parâmetro e a preencha com valores numéricos
# até que seja digitado ponto (.).

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
print(lista)