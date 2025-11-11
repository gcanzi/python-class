#Gustavo Moretim Canzi - RM 567683
#27/10/2025

# 2 - Dado um numero, exibir o seu fatorial: 4! = 4 . 3 . 2 . 1 = 24

num = int(input("Número: "))
fat = 1

for i in range(1, num + 1):
    fat = fat * i

print(f"Fatorial: {fat}")