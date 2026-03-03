'''Faça um programa que crir uma lista vazia e peça para o usuário digitar elementos até digitar o caractere '.' (ponto).
 Ao final exibir o conteúdo da lista'''

import os
os.system("cls")

print("Digite algo ou . para finalizar:")

list = list()
x = ""

while x != '.':
    x = input("-> ")

    if x != '.':
        list.append(x)

print(list)