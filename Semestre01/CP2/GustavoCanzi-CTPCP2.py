#Gustavo Moretim Canzi - RM 567683
#27/10/2025

somaTurma = 0
alunosAprovados = 0
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
            if nota < -1 or nota > 10:
                while nota >= 0:
                    nota = int(input("Digite uma nota valida entre 0 e 10. Nota: "))
            if nota == -1 and volta < 2:
                while nota < 0:
                    nota = int(input("Digite uma nota valida entre 0 e 10. Nota: "))
            if nota == -1:
                break
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

alunosReprovados = float((reprovado / volta) * 100)

print()
print(f"Média da turma: {mediaTurma:.1f}")
print()
print(f"Qtd. Aprovados: {aprovado} - {alunosAprovados:.1f}%")
print(f"Qtd. Exames: {exame} - {alunosReprovados:.1f}%")
print(f"Qtd. Reprovados: {reprovado} - {alunosReprovados:.1f}%")