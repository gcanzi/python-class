# Crie uma função chamada converter_dolar(valor_reais, cotacao_dolar) que receba um valor em reais e retorne o
# valor convertido para dólares.

import os
os.system("cls")

dolar = float(input("Digite o valor para ser convertido em dolar: "))

def converterDolar(conv: float) -> float:
    return float(conv / 5.7)

print(f"A quantidade de dólar é {converterDolar(dolar):.2f}")
