#Gustavo Moretim Canzi - RM 567683
#27/10/2025

somaTurma = 0
alunosAprovados = 0
alunosExames = 0
alunosReprovados = 0
aprovado = 0
reprovado = 0
exame = 0
nota = 0

for volta in range(1, 11):
    print(f"ALUNO {volta}:")
    print()
    soma = 0
    for volta2 in range(1,3):
        print("Digite a nota do Aluno:")
        nota = float(input(f"Nota {volta2}: "))
        # Se for -1 na Nota 1 do primeiro aluno → inválido
        if nota == -1 and volta == 1 and volta2 == 1:
            print("Digite uma nota válida entre 0 e 10.")
            nota = float(input(f"Nota {volta2}: "))

        # Se for -1 (apenas a partir do segundo aluno) → encerra
        if nota == -1 and volta2 == 1 and volta > 1:
            parar = 1
            break

        # Se for inválida → repetir
        while nota < 0 or nota > 10:
            print("Digite uma nota válida entre 0 e 10.")
            nota = float(input(f"Nota {volta2}: "))
            
        soma = soma + nota
    if nota == -1:
        parar = 1
        break

    media = float(soma / 2)
    somaTurma = float(somaTurma + media)
    if media >= 6:
        print(f"Aprovado com média {media}")
        print()
        print("-----------------")
        print()
        aprovado = aprovado + 1
    elif media >= 4:
        print(f"Exame com média {media}")
        print()
        print("-----------------")
        print()
        exame = exame + 1
    else:
        print(f"Reprovado com média {media}")
        print()
        print("-----------------")
        print()
        reprovado = reprovado + 1

if parar == 1:
    volta = volta - 1

mediaTurma = float(somaTurma / volta)
alunosAprovados = float((aprovado / volta) * 100)
alunosExames = float((exame / volta) * 100) #2
alunosReprovados = float((reprovado / volta) * 100)

print()
print(f"Média da turma: {mediaTurma:.1f}")
print()
print(f"Qtd. Aprovados: {aprovado} - {alunosAprovados:.1f}%")
print(f"Qtd. Exames: {exame} - {alunosExames:.1f}%") #1
print(f"Qtd. Reprovados: {reprovado} - {alunosReprovados:.1f}%")