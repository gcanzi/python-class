import os
os.system("cls")

'''
Forma 1 -> Importando todos os subalgoritmos
Vantagem -> Importa todos os subalgoritmos
Desvatagem -> Importa todos os subalgoritmos
'''

import funcoes as f

# ==== PRINCIPAL

valor1 = 10
valor2 = 3 

print("Soma = ", f.calcsoma(valor1, valor2))
print("Subtração = ", f.calcsubtracao(valor1, valor2))
print("Multiplicação = ", f.calcmultiplicacao(valor1, valor2))
resp = f.calcdivisao(valor1, valor2)
print(f"Divisão = {resp:.2f}")