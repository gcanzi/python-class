# Crie uma função chamada quadrado(numero) que receba um número e retorne o valor dele ao quadrado.
import os
os.system("cls")

numero = int(input("Digite um número: "))

# o num é apenas a referencia de um valor que vai receber
def quadrado(num: int) -> int:
    return num ** 2

# para chamar a função precisa colocar o que quiser modificar dentro do parenteses da função
print(f"O valor ao quadrado de {numero} é {quadrado(int(numero))}")
