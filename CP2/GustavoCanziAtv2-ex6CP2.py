#Gustavo Moretim Canzi - RM 567683
#27/10/2025

# 6 - Dados dois números que representam um intervalo e a ordem C para crescente ou D para decrescente, exiba os números
# do intervalo na ordem escolhida.

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
ordem = str(input("Ordem: "))

if ordem == "C":
    print("Multiplos: ")
    volta = inicio
    for volta in range(inicio, fim + 1, 1):
        print(volta, end=" ") 
else:
    print("Multiplos: ")
    volta = inicio
    for volta in range(fim, inicio - 1, -1):
        print(volta, end=" ")