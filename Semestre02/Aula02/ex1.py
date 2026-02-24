'''
Utilizando somente os metodos e funções explicados até o momento, faça um programa que pegue uma lista com itens distintos e crie outras duas listas,
uma em ordem crescente e a outra em ordem decrescente.'''

import os
os.system("cls")

lista = [ 34, 23, -11, 45, 12]
print("Lista original........", lista)

lCrescente = lista.copy()
lCrescente.sort()
print("Lista crescente.......", lCrescente)

lDecrescente = lista.copy()
lDecrescente.sort(reverse=True)
print("Lista decrescente.....", lDecrescente)