# Exercicios:
# 1. Dado um numero por parâmetro, retorne o dobro
# >> resp = dobro(5) # resp valerá 10 

# 2. Fazer uma função que calcule o valor de delta. (pense quantos e quais parametros são necessários)
# >> resp = delta (1,2,3) # resp valerá -8 

# 3. Fazer uma função que calcule a media de 4 numeros. (pense quantos e quais parametros são necessários)
# >> resp = media4n(8,9,10,7) # resp valerá 8.5

# 4. Dados por parâmetro um número e um multiplo, exiba p próximo múltiplo do primeiro numero.
# >> resp = prox_mult(22, 7) # resp valerá 28

import os
os.system("cls")

# 1
def numDobro():
    num = 5
    return num * 2
print(numDobro())

# 2
def delta():
    a = 1
    b = 2
    c = 3

    delta = (b ** 2) - 4 * a * c

    return delta
print(delta())

# 3
def media4n():
    num1 = 8
    num2 = 9
    num3 = 10
    num4 = 7

    return (num1 + num2 + num3 + num4) / 4
print(media4n())

# 4
def proxMultiplo():
    num1 = 7
    num2 = 22

    return num2 // num1 * num1 + num1
print(proxMultiplo())