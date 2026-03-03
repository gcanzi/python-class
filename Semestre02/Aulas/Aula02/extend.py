import os
os.system("cls")

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l2.extend(l1)

# .extend = ele adiciona a uma lista, os elementos de outra já existente

print(l1, l2)