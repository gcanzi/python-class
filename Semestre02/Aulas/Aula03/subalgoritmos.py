
# Criação de função
def retornaMaior(num1, num2, num3):
    maior = 0
    if n1 > maior:
        maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3

    return maior

#Programa principal
import os 
os.system("cls")

# Dados 3 números, retornar o de maior valor

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

print(retornaMaior(n1, n2, n3))