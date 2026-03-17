#Gustavo Moretim Canzi - RM567683
# 09/03/2026

import os
os.system("cls")

lista = []

while True:

    os.system("cls")

    print("MENU\n")
    print("1 - Cadastrar preços")
    print("2 - Remover preços")
    print("3 - Exibir relatório dos preços")
    print("4 - Organizar lista dos preços")
    print("0 - SAIR")

    escolha = input("\nEscolha: ")

    match escolha:

        case '0':
            break
        case '1':
            
            qtd = int(input("\nQuantidade de preços: "))

            for i in range(qtd):
                lista.append(float(input("Preço: ")))

            print(f"\nLista de preços: {lista}")
            copia = lista.copy()
            print(f"Cópia da lista: {copia}")

        case '2':

            print("\nA - Último elemento")
            print("B - Digitar o preço a ser removido")

            opcao = input("\nEscolha: ")

            if opcao == 'a' or opcao == 'A':
                
                qtd_elementos = len(lista)

                if len(lista) > 0:
                    lista.pop(qtd_elementos - 1)

                    print(f"Item removido: {copia[qtd_elementos - 1]}")
                    copia.pop(qtd_elementos - 1)
                else:
                    print("A lista esta vazia!")
     
            elif opcao == 'b' or opcao == 'B':

                remover = float(input("Preço: "))

                contador = lista.count(remover)

                if contador == 0:
                    print("Este preço não esta cadastrado!")
                else:
                    lista.remove(remover)
                    copia.remove(remover)
                    print("Removido com sucesso!")

            else:
                print("Opção invalida")

        case '3':

            print(f"Cópia da lista: {copia}")
            qtd_elementos = len(copia)
            print(f"Quantidade de preços: {len(copia)}")
            soma = sum(copia)
            media = soma / qtd_elementos
            print(f"Média dos preços: {media:.2f}")

            preco = float(input("\nPreço: "))
            indice = copia.index(preco)
            print(f"Posição do primeiro: {indice}")
            contador = copia.count(preco)
            print(f"Quantas vezes: {contador}")
        
        case '4':

            print(f"Lista de preços {lista}")
            lCrescente = lista.copy()
            lCrescente.sort()
            print(f"Crescente: {lCrescente}")
            lDecrescente = lista.copy()
            lDecrescente.sort(reverse=True)
            print(f"Decrescente: {lDecrescente}")
            lInvertida = lista.copy()
            lInvertida.reverse()
            print(f"Invertida: {lInvertida}")
            
        case _ :
            "Número inválido!"
        
    input("\nDigite algo para voltar . . . ")
    