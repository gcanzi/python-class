# Gustavo Moretim Canzi
# 23/02/2026

import os
os.system("cls")

lista = []
lista_numerica = []
lista_random = []
elem = ""
soma = 0

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
                if elem.isnumeric() == False:
                    lista_random.append(elem)
                else:
                    int(lista_numerica.append(elem))
        case '3':
            for elem in lista_numerica:
                soma = soma + elem

            print("a - A soma dos valores: ", soma)

            print("b - Quantos elementos tem na lista: ", len.list())

            lCrescente = lista.copy()
            lCrescente.sort()
            print("c - Lista em ordem crescente: ", lCrescente)

            lDecrescente = lista.copy()
            lDecrescente.sort(reverse=True)
            print("d - Lista em ordem decrescente: ", lDecrescente)

        case '4':
            print("Esse elemento não existe.")
        case '5':
            print(lista)
            print(lista_numerica)
            print(lista_random)
        case _ :
            "Número inválido!"
    
    input("\nDigite algo para voltar . . . ")