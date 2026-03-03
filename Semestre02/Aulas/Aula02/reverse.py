import os 
os.system("cls")

# Exemplo 1: Invertendo uma lista com .reverse()
# nesse exemplo, inverteu os elementos da lista
frutas = ["maça", "banana", "cereja"]
frutas.reverse()
print(frutas) # Saida: ["cereja", "banana", "maça"]

# Exemplo 2: Usando reversed() para criar uma nova lista (sem alterara a original)
#neste caso, ele inverteu os valores, sem que alterasse nos valores originais
numeros = [1, 45, 13, 4]
numeros_invertidos = list(reversed(numeros))
print(numeros)  # Saida: [1, 45, 13, 4]
print(numeros_invertidos)  # Saida: [4, 13, 45, 1]
