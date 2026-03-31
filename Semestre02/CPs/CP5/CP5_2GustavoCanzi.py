# Gustavo Moretim Canzi
# RM 567683

import os
os.system("cls")

aluno = []
nota1 = []
nota2 = []
media = []

while True:

    os.system("cls")

    print("MENU\n")
    print("1 - Preencher as notas")
    print("2 - Exibir o registro do aluno")
    print("3 - Exibir os registros")
    print("4 - Contar aprovados e reprovados")
    print("0 - SAIR")

    escolha = input("\nEscolha: ")

    match escolha:

        case '0':
            break

        case '1':

            qtd = int(input("\nQuantidade de alunos: "))

            for i in range(qtd):
                nome = input("Nome do aluno: ")
                n1 = float(input("Nota 1: "))
                n2 = float(input("Nota 2: "))

                mediaSoma = (n1 + n2) / 2

                aluno.append(nome)
                nota1.append(n1)
                nota2.append(n2)
                media.append(mediaSoma)

            print("\nCadastro realizado com sucesso!")

        case '2':

            if len(aluno) == 0:
                print("\nNenhum aluno cadastrado!")
            else:
                nome_busca = input("\nDigite o nome do aluno: ")

                if nome_busca in aluno:
                    pos = aluno.index(nome_busca)

                    print(f"\nNome: {aluno[pos]}")
                    print(f"Nota 1: {nota1[pos]}")
                    print(f"Nota 2: {nota2[pos]}")
                    print(f"Média: {media[pos]:.2f}")

                    if media[pos] >= 6:
                        print("Status: Aprovado")
                    else:
                        print("Status: Reprovado")
                else:
                    print("Aluno não encontrado!")

        case '3':

            if len(aluno) == 0:
                print("\nNenhum registro cadastrado!")
            else:
                for i in range(len(aluno)):

                    print(f"\nNome: {aluno[i]}")
                    print(f"Nota 1: {nota1[i]}")
                    print(f"Nota 2: {nota2[i]}")
                    print(f"Média: {media[i]:.2f}")

                    if media[i] >= 6:
                        print("Status: Aprovado")
                    else:
                        print("Status: Reprovado")

        case '4':

            if len(media) == 0:
                print("\nNenhum registro cadastrado!")
            else:
                aprovados = 0
                reprovados = 0

                for m in media:
                    if m >= 6:
                        aprovados += 1
                    else:
                        reprovados += 1

                print(f"\nAprovados: {aprovados}")
                print(f"Reprovados: {reprovados}")

        case _:
            print("Opção inválida!")

    input("\nDigite algo para voltar . . . ")