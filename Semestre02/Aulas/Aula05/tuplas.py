import os
os.system("cls")

# Tuplas - é uma "lista" cujo conteudo não pode ser modificado
lista = list()
tupla = tuple() # tupla vazia
lista = [1,2,3,4,5]
tupla = (6,7,8,9,0) # tupla com valores

for elem in lista:
    print("Lista: ", elem)

print()

for elem in tupla:
    print("Tupla: ", elem)

lista[0] = 99
print(lista)
# tupla[0] = 99
print(tupla)