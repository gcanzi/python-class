def obter_nota(numero):
    """Lê uma nota válida entre 0 e 10."""
    while True:
        try:
            nota = float(input(f"Nota {numero}: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Digite uma nota válida entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 0 e 10.")


def main():
    total_medias = 0
    qtd_alunos = 0
    aprovados = exames = reprovados = 0

    while True:
        print(f"\nALUNO {qtd_alunos + 1}")

        # Leitura da primeira nota
        try:
            nota1 = float(input("Nota 1: "))
        except ValueError:
            print("Digite uma nota válida entre 0 e 10.")
            continue

        # Verifica se é o encerramento do programa
        if nota1 == -1:
            if qtd_alunos == 0:
                print("Nota inválida. É necessário ter pelo menos um aluno válido.")
                continue
            else:
                break

        # Caso a nota 1 seja inválida
        while nota1 < 0 or nota1 > 10:
            print("Digite uma nota válida entre 0 e 10.")
            nota1 = obter_nota(1)

        # Leitura da segunda nota
        nota2 = obter_nota(2)

        media = (nota1 + nota2) / 2
        total_medias += media
        qtd_alunos += 1

        # Verificação da situação do aluno
        if media >= 6:
            print(f"APROVADO com média {media:.1f}")
            aprovados += 1
        elif 4 <= media < 6:
            print(f"EXAME com média {media:.1f}")
            exames += 1
        else:
            print(f"REPROVADO com média {media:.1f}")
            reprovados += 1

        print("-" * 25)

        # Interrupção opcional se já houver 10 alunos
        if qtd_alunos >= 10:
            print("Limite máximo de 10 alunos atingido.")
            break

    # Cálculos finais
    media_turma = total_medias / qtd_alunos
    print("\n---------------------------")
    print(f"Média da turma: {media_turma:.2f}")
    print("---------------------------")

    print(f"Qtd. Aprovados: {aprovados} - {aprovados / qtd_alunos * 100:.1f}%")
    print(f"Qtd. Exames: {exames} - {exames / qtd_alunos * 100:.1f}%")
    print(f"Qtd. Reprovados: {reprovados} - {reprovados / qtd_alunos * 100:.1f}%")


if __name__ == "__main__":
    main()
