# # para treino, faça uma versão com cada laço.
# Dados dois numeros pelo usuario (inicio e fim), exiba os numeros do inicio ao fim
#Se o fim for maior que o inicio, exibir de forma decrescente, caso não, exibir normal.
"""

inicio: 7
fim: 12

7 8 9 10 11 12

inicio: 12
fim: 7

12 11 10 9 8 7

"""

inicio = int(input("Quer iniciar em qual número? "))
fim = int(input("Quer ir até qual? "))

if inicio < fim:
    print("Sequencia com o while")
    volta = inicio
    while volta <= fim:
        print(volta)
        volta = volta + 1

    print("Sequencia com o while True")
    volta = inicio
    while True:
        print(volta)
        volta = volta + 1
        if volta > fim:
            break

    print("Sequencia com o for")
    volta = inicio
    for volta in range(inicio, fim + 1, 1):
        print(volta) 
else:
    print("Sequencia com o while")
    volta = inicio
    while volta >= fim:
        print(volta)
        volta = volta - 1

    print("Sequencia com o while True")
    volta = inicio
    while True:
        print(volta)
        volta = volta - 1
        if volta < fim:
            break

    print("Sequencia com o for")
    volta = inicio
    for volta in range(inicio, fim - 1, -1):
        print(volta) 