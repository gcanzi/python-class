#Gustavo Moretim Canzi - RM 567683
#27/10/2025

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))

print("Mult 5:", end=" ")

for i in range(inicio, fim):
    if i % 5 == 0:
        print(i, end=" ")