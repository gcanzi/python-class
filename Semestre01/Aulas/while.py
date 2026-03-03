# Exercicio:
# 1- Dadas duas notas pelo usuário, calcular a media e exibir.
# Ao final perguntas: Deseja continuar ? <s>im ou <n>ão?
# Ao final exibir quantas médias foram calculadas.

import os
quantidade = 0 
opcao = 's'

while opcao == 's':
    os.system("cls")
    print("Digite duas notas: ")
    nota1 = float(input("Nota1 = "))
    nota2 = float(input("Nota2 = "))
    media = (nota1 + nota2) /2
    print(f"A média de {nota1} com {nota2} é {media}")
    quantidade = quantidade + 1
    opcao = input("Deseja continuar ? <s>im ou <n>ão?")

print(f"Voce executou o programa {quantidade} vezes")