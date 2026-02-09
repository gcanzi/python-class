# Gustavo Moretim Canzi
# 07/11/2025

import os
os.system("cls")

vagas = [0,0,0,0,0,0,0,0,0,0] 

while True:

    print("1 - Mostrar estado das vagas.")
    print("2 - Ocupar uma vaga.")
    print("3 - Liberar uma vaga.")
    print("4 - Encerrar o programa.\n")

    opcao = int(input("Escolha: "))
    print("")

    if opcao < 1 or opcao > 4:
        while opcao < 1 or opcao > 4:
            opcao = int(input("Opção inválida, digite um valor entre 1 e 4: "))
        print()

    if opcao == 1:
        for i in range(10):
            print(f"Vaga {i+1}: ", end="")
            if vagas[i] == 0:
                print("Livre")
            else:
                print("Ocupada")
    elif opcao == 2:
        posicao = int(input("Qual vaga pretende ocupar? "))
        while posicao < 1 or posicao > 10:
            print("Numero de vagas inválido, escolha entre 1 e 10.")
            posicao = int(input("Qual vaga pretende ocupar? "))
        if vagas[posicao-1] == 0:
            print("\nVaga ocupada com sucesso!")
            vagas[posicao-1] = 1
        else:
            print("\nEssa vaga já está ocupada.")
    elif opcao == 3:
        posicao = int(input("Qual vaga pretende deixar livre? "))
        while posicao < 1 or posicao > 10:
            print("Numero de vagas inválido, escolha entre 1 e 10.")
            posicao = int(input("Qual vaga pretende deixar livre? "))
        if vagas[posicao-1] == 1:
            print("\nVaga liberada com sucesso!")
            vagas[posicao-1] = 0
        else:
            print("\nEssa vaga já está livre.")
    elif opcao == 4:
        break        

    input("\nPressione qualquer tecla para continuar . . .")
    os.system("cls")
