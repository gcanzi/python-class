import os
os.system("cls")

from funcoes import *

# ==== PRINCIPAL

valor1 = 10
valor2 = 3

print("Soma = ", calcsoma(valor1, valor2))
print("Subtração = ", calcsubtracao(valor1, valor2))
print("Multiplicação = ", calcmultiplicacao(valor1, valor2))
print(f"Divisão = {calcdivisao(valor1, valor2):.2f}")