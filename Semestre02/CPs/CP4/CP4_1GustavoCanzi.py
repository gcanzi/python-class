# Gustavo Moretim Canzi
# 09/02/2026

import os
os.system("cls")

while True:

    os.system("cls")

    print("MENU\n")
    print("0 - SAIR")
    print("1 - Criar / Iniciar uma lista")
    print("2 - Inserir um elemento na lista")
    print("3 - Inserir elementos até digitar ponto (.)")
    print("4 - Remover elemento pelo índice")
    print("5 - Remover elemento pelo conteúdo")
    print("6 - Exibir a lista")
    print("7 - Remover todos os itens de um elemento existente")

    escolha = input("\nEscolha uma opção: ")

    match escolha:
        case '0':
            break
        case '1':
            lista = []
            elem = ""
        case '2':
            elem = input("-> ")
            lista.append(elem)
        case '3':
            while elem != '.':
                elem = input("-> ")
                if elem != '.':
                    lista.append(elem)
        case '4':
            x = int(input("\nDigite a posição do elemento que deseja remover: "))
            qtd_elementos = len(lista)

            if (0 <= x) and (x < qtd_elementos):
                lista.pop(x)
            else:
                print("Esse elemento não existe.")
        case '5':
            x = input("\nDigite o conteúdo do elemento que deseja remover: ")
            if lista.count(x) != 0:
                lista.remove(x)
            else:
               print("Esse conteúdo não existe.") 
        case '6':
            print(lista)
        case '7':
            x = input("\nDigite o conteúdo do elemento que deseja remover: ")

            if x in lista:
                while x in lista:
                    lista.remove(x)
            else:
                print("Esse elemento não existe na lista.")
        case _ :
            "Número inválido!"
    
    input("\nDigite algo para voltar . . . ")