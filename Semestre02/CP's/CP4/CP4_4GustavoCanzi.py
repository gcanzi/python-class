#Gustavo Moretim Canzi - RM567683
# 09/03/2026

import os
os.system("cls")

lista = []
elem = ""

while elem != 0:
    elem = int(input("-> "))
    if elem != 0:
        lista.append(elem)

print(f"Lista = {lista}")

print("\nCrescente:")
lCrescente = lista.copy()
lCrescente.sort()
print(f"Intervalo fechado: {lCrescente}")
print("Intervalo aberto: ]", end="")
for i in range(1,len(lCrescente)-1):
    print(f"{lCrescente[i]},", end=" ")
print("[")

print(f"\nDecrescente:")
lDecrescente = lista.copy()
lDecrescente.sort(reverse=True)
print(f"Intervalo fechado: {lDecrescente}")
print("Intervalo aberto: ]", end="")
for i in range(1,len(lDecrescente)-1):
    print(f"{lDecrescente[i]},", end=" ")
print("[")
