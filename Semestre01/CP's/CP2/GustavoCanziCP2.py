#Gustavo Moretim Canzi - RM 567683
#20/10/2025

qtdAlunos = int(input("Quantidade de alunos: "))
somaTurma = 0
alunosAprovados = 0
alunosReprovados = 0
aprovado = 0
reprovado = 0

for volta in range(1, qtdAlunos + 1):
    print(f"ALUNO {volta}/{qtdAlunos}:")
    print()
    soma = 0
    for volta2 in range(1,3):
        nota = int(input(f"Nota {volta2}: "))
        while nota < 0 or nota > 10:
            nota = int(input(f"Digite uma nota valida entre 0 e 10. Nota {volta2}: "))
        soma = soma + nota
    media = float(soma / 2)
    print()
    somaTurma = float(somaTurma + media)
    if media >= 6:
        print(f"Aprovado com média {media}")
        print()
        aprovado = aprovado + 1
    else:
        print(f"Reprovado com média {media}")
        print()
        reprovado = reprovado + 1

mediaTurma = float(somaTurma / qtdAlunos)
alunosAprovados = float((aprovado / qtdAlunos) * 100)
alunosReprovados = float((reprovado / qtdAlunos) * 100)

print("DADOS CONSOLIDADOS")
print()
print(f"Média da turma: {mediaTurma:.1f}")
print(f"Aprovados: {alunosAprovados:.1f}%")
print(f"Reprovados: {alunosReprovados:.1f}%")