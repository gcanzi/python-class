import os
os.system("cls")

'''
Forma 1 -> Importando todos os subalgoritmos
Vantagem -> Importa todos os subalgoritmos
Desvatagem -> Importa todos os subalgoritmos
'''

import funcoes
# from funcoes import calcsoma, calcsubtracao

# ==== PRINCIPAL

valor1 = 10
valor2 = 3 #0

print("Soma = ", funcoes.calcsoma(valor1, valor2))
print("Subtração = ", funcoes.calcsubtracao(valor1, valor2))
print("Multiplicação = ", funcoes.calcmultiplicacao(valor1, valor2))
print(f"Divisão = {funcoes.calcdivisao(valor1, valor2):.2f}")