import os
os.system("cls")

# .copy = copia os valores de uma lista para a outra
# pq n usar o "="? porque no caso da lista, ele n copia o valor e sim faz o apontamento do endereço da variavel, sendo assim independete do valor que
#tiver, ele será descartado pois n existe mais sua referência.

l1 = [1, 3, 5]
l2 = [2, 4, 6]

print(l1 ,l2)
print("------------------------------\n")

l1 = [1, 3, 5]
l2 = l1.copy()

print(l1 ,l2)
print("------------------------------\n")

l1.append(7)
l2.append(8)

print(l1 ,l2)
print("------------------------------\n") 