# Crie uma função chamada maior(a, b, c) que receba três números e retorne qual deles é o maior.

import os
os.system("cls")

a = input("Digite um número: ")
b = input("Digite um número: ")
c = input("Digite um número: ")

def maior(a: float, b: float, c: float) -> float:
    # maiornum é uma variavel local que só funciona dentro da função
    if a > b and a > c:
        maiornum = a
    elif b > a and b > c:
        maiornum = b
    else:
        maiornum = c
    
    return maiornum

print("O maior é", maior(a, b, c))