# Gustavo Moretim Canzi - Gustavo Castilho Gonçalves
# RM 567683             - RM 566970
# 06/04/2026

import os
os.system("cls")

def listaNumerica(l: list) -> list:
    listaNum = []

    for elem in l:
        if elem.isdigit():
            listaNum.append(int(elem))
        else:
            if len(elem) > 1:
                if elem[0] == '-':
                    if elem[1:].isdigit():
                        listaNum.append(int(elem))

    return listaNum


def listaOutros(l: list) -> list:
    listaOutros = []

    for elem in l:
        num = False

        if elem.isdigit():
            num = True
        else:
            if len(elem) > 1:
                if elem[0] == '-':
                    if elem[1:].isdigit():
                        num = True

        if num == False:
            listaOutros.append(elem)

    return listaOutros


def preencherLista(l: list) -> None:
    print("\nDigite os elementos da lista ou '.' para finalizar...")

    while True:
        elem = input()

        if elem == '.':
            listaNum = listaNumerica(l)
            listaOutrosLista = listaOutros(l)

            print("\na.")
            print(f"lista completa = {l}")
            print(f"Lista numérica = {listaNum}")
            print(f"Lista outros = {listaOutrosLista}")

            if len(listaNum) > 0:
                soma = sum(listaNum)
                media = soma / len(listaNum)

                print("\nb.")
                print(f"Soma da lista numérica = {soma}")
                print(f"Media da lista numérica = {media:.2f}")
                print(f"Maior valor = {max(listaNum)}")
                print(f"Menor valor = {min(listaNum)}")
            else:
                print("\nNenhum número foi inserido.")

            break
        else:
            l.append(elem)


def buscarNumero(l: list) -> None:
    listaNum = listaNumerica(l)

    if len(listaNum) == 0:
        print("\nLista numérica vazia!")
        return

    n = input("\nDigite um número: ")

    num = False

    if n.isdigit():
        num = True
    else:
        if len(n) > 1:
            if n[0] == '-':
                if n[1:].isdigit():
                    num = True

    if num == False:
        print("Valor inválido!")
        return

    n = int(n)

    if n in listaNum:
        print(f"Encontrou o {n}!")
    else:
        maisProximo = listaNum[0]

        if listaNum[0] - n < 0:
            menorDiferenca = (listaNum[0] - n) * -1
        else:
            menorDiferenca = listaNum[0] - n

        for valor in listaNum:
            if valor - n < 0:
                diferenca = (valor - n) * -1
            else:
                diferenca = valor - n

            if diferenca < menorDiferenca:
                menorDiferenca = diferenca
                maisProximo = valor

        print(f"O mais próximo é o {maisProximo}!")


def analisarString() -> None:
    frase = input("\nDigite uma frase: ")

    palavras = len(frase.split())
    vogais = 0
    digitos = 0
    especiais = 0

    for c in frase:
        if c.lower() in "aeiou":
            vogais += 1
        else:
            if c.isdigit():
                digitos += 1
            else:
                if c != ' ':
                    if c.lower() < 'a' or c.lower() > 'z':
                        especiais += 1

    print("\nNesta frase tem:")
    print(f"a. {palavras} palavras")
    print(f"b. {vogais} vogais (maiúsculas ou minúsculas)")
    print(f"c. {digitos} dígitos")
    print(f"d. {especiais} caracteres especiais")


# ---------------- PROGRAMA PRINCIPAL ---------------- #

lista = []

while True:
    print("\n0 - SAIR")
    print("1 - Exercício Lista")
    print("2 - Exercício String")

    escolha = input("\nEscolha: ")

    match escolha:
        case '1':
            lista.clear()
            preencherLista(lista)
            buscarNumero(lista)

        case '2':
            analisarString()

        case '0':
            print("\nEncerrando...")
            break

        case _:
            print("\nOpção inválida!")