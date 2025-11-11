# # para treino, faça uma versão com cada laço.
# Dados dois numeros pelo usuario (inicio e fim), exiba os numeros do inicio ao fim
"""

inicio: 4
fim: 18

4 5 6 7 8 9 10 11 12 13 14 15 16 17 

"""

inicio = int(input("Quer iniciar em qual número? "))
fim = int(input("Quer ir até qual? "))

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