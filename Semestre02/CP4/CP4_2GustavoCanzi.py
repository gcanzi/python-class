# Gustavo Moretim Canzi
# 23/02/2026

import os
os.system("cls")

lista = []
lista_numerica = []
lista_random = []
elem = ""

while True:

    os.system("cls")

    print("MENU\n")
    print("0 - SAIR")
    print("1 - Insira elementos na lista ou digite ponto (.) para sair.")
    print("2 - Separe a lista entre elementos inteiros e os demais.")
    print("3 - Exibir dados da lista numérica.")
    print("4 - Junte os dados das listas em ordem crescente e os demais no final.")

    escolha = input("\nEscolha uma opção: ")

    match escolha:
        case '0':
            break
        case '1':
            while elem != '.':
                elem = input("-> ")
                if elem != '.':
                    lista.append(elem)
        case '2':
            for elem in lista:
                while not elem.isnumeric():
                    lista_random.append(elem)
                else:
                    lista_numerica.append(elem)
        case '3':
            print()
        case '4':
            x = int(input("\nDigite a posição do elemento que deseja remover: "))
            qtd_elementos = len(lista)

            if (0 <= x) and (x < qtd_elementos):
                lista.pop(x)
            else:
                print("Esse elemento não existe.")
        case '5':
            print(lista)
            print(lista_numerica)
            print(lista_random)
        case _ :
            "Número inválido!"
    
    input("\nDigite algo para voltar . . . ")