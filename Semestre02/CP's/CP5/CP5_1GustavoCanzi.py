# Gustavo Moretim Canzi - RM567683
# 16/03/2026

'''
Exercício 7:
Crie uma função chamada contar_pares(lista) que receba uma lista de números e retorne quantos números pares existem nela.
 
Exercício 8:
Crie uma função chamada numeros_acima_media(lista) que receba uma lista de números.
A função deve calcular a média da lista e retornar uma nova lista contendo apenas os números que estão acima da média.

Exercício 9:
Crie uma função chamada remover_negativos(lista) que receba uma lista de números e remova todos os valores negativos utilizando métodos de lista.
A função deve retornar a lista sem números negativos.

Exercício 10
Crie um função chamada retorna_mais_proximo(lista, valor) que se não encontrar o valor igual retorne o mais próximo contido na lista. 
'''
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

def contarPares(l: list) -> int:
    contador = 0
    for i in range(0, len(lista)):
        if (l[i] % 2) == 0:
            contador += 1
    return contador

# 7
print(f"A quantidade de números pares é {contarPares(lista)}")

def numerosAcimaDaMedia(l: list) -> list:
    media = sum(l) / len(l)
    mediaLista = []
    for i in range(0, len(l)):
        if media < l[i]:
            mediaLista.append(l[i])

    return mediaLista

#8
print(f"\nA lista com os valores acima da média é {numerosAcimaDaMedia(lista)}")

