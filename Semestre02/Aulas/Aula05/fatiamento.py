import os
os.system("cls")

# fatiamento
# Sintaxe: lista[inicio : fim : passo]
#           0   1   2   3   4   5   6   7   8   9
#         -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numeros)
print(numeros[3:7]) # só conta o que estiver dentro do estimado, a posição em si, não conta
numerosParte = numeros[3:7] # grava uma nova lista só com a parte apontada
print(numerosParte)
print(numeros[-4:-1]) # ele tambem pode contar a lista de tras p frente com os numeros negativos

print(numeros[1:8:3]) # desta forma pode chamar a lista pelas posições | da posição 1 até a 8, pulando de 3 em 3
print(numeros[8:1:-2]) # crescente ou decrescente

print(numeros[::]) # imprime toda a lista
print(numeros[-3::]) # imprime do -3 até ao final da lista
print(numeros[::-1]) # imprime em ordem decrescente


