# Gustavo Moretim Canzi
# RM 567683

import os
os.system("cls")

# Listas

aluno = []
nota1 = []
nota2 = []
media = []

# Entradas

def isint(v: str) -> bool:
    if len(v) == 0:
        return False
        
    if v[0] == '-':
        v = v.replace('-', '', 1)
    elif v[0] == '+':
        v = v.replace('+', '', 1)
        
    return v.isdigit()

def isfloat(v: str) -> bool:
    if len(v) == 0:
        return False
        
    if v[0] == '-':
        v = v.replace('-', '', 1)
    elif v[0] == '+':
        v = v.replace('+', '', 1)
        
    v = v.replace('.', '', 1)
    return v.isdigit()

def ler_inteiro(texto: str) -> int:
    while True:
        entrada = input(texto)
        if isint(entrada):
            numero = int(entrada)
            if numero > 0:
                return numero
        print("Entrada inválida! Digite um número inteiro maior que zero.")

def ler_nome(texto: str) -> str:
    while True:
        nome = input(texto)
        palavras = nome.split()
        if len(palavras) >= 2:
            return nome
        print("Nome inválido! Digite pelo menos nome e sobrenome.")

def ler_nota(texto: str) -> float:
    while True:
        entrada = input(texto)
        entrada = entrada.replace(',', '.', 1)
        
        if isint(entrada) or isfloat(entrada):
            nota = float(entrada)
            if nota >= 0 and nota <= 10:
                return nota
                
        print("Nota inválida! Digite um número entre 0 e 10.")

# Procedimentos

def exibir_boletim(pos: int, aluno: list, nota1: list, nota2: list, media: list) -> None:
    print(f"\nNome: {aluno[pos]}")
    print(f"Nota 1: {nota1[pos]}")
    print(f"Nota 2: {nota2[pos]}")
    print(f"Média: {media[pos]:.2f}")
    if media[pos] >= 6:
        print("Status: Aprovado")
    else:
        print("Status: Reprovado")

def cadastrar_alunos(aluno: list, nota1: list, nota2: list, media: list) -> None:
    qtd = ler_inteiro("\nQuantidade de alunos a cadastrar: ")

    for i in range(qtd):
        print(f"\n--- Cadastro do Aluno {i+1} ---")
        nome = ler_nome("Nome do aluno: ")
        n1 = ler_nota("Nota 1: ")
        n2 = ler_nota("Nota 2: ")

        media_soma = (n1 + n2) / 2

        aluno.append(nome)
        nota1.append(n1)
        nota2.append(n2)
        media.append(media_soma)

    print("\nCadastro(s) realizado(s) com sucesso!")

def buscar_aluno(aluno: list, nota1: list, nota2: list, media: list) -> None:
    if len(aluno) == 0:
        print("\nNenhum aluno cadastrado!")
        return

    nome_busca = input("\nDigite o nome exato do aluno: ")

    if nome_busca in aluno:
        pos = aluno.index(nome_busca)
        exibir_boletim(pos, aluno, nota1, nota2, media)
    else:
        print("\nAluno não encontrado!")

def exibir_todos(aluno: list, nota1: list, nota2: list, media: list) -> None:
    if len(aluno) == 0:
        print("\nNenhum registro cadastrado!")
        return

    print("\n=== TODOS OS REGISTROS ===")
    for i in range(len(aluno)):
        exibir_boletim(i, aluno, nota1, nota2, media)

def estatisticas(media: list) -> None:
    if len(media) == 0:
        print("\nNenhum registro cadastrado!")
        return

    aprovados = 0
    reprovados = 0

    for m in media:
        if m >= 6:
            aprovados += 1
        else:
            reprovados += 1

    print("\n=== ESTATÍSTICAS DA TURMA ===")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}")

# Programa principal

while True:
    os.system("cls")

    print("=================================")
    print("             MENU                ")
    print("=================================")
    print("1 - Preencher as notas")
    print("2 - Exibir o registro do aluno")
    print("3 - Exibir os registros")
    print("4 - Contar aprovados e reprovados")
    print("0 - SAIR")
    print("=================================")

    escolha = input("\nEscolha: ")

    match escolha:
        case '0':
            print("\nEncerrando...")
            break
        case '1':
            cadastrar_alunos(aluno, nota1, nota2, media)
        case '2':
            buscar_aluno(aluno, nota1, nota2, media)
        case '3':
            exibir_todos(aluno, nota1, nota2, media)
        case '4':
            estatisticas(media)
        case _:
            print("\nOpção inválida!")

    input("\nDigite algo para voltar . . . ")