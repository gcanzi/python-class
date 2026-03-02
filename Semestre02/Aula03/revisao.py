import os
os.system("cls")

#Remover pelo indice
'''
lista = ["fiap", 65, True, 25, 68.8, "Engenharia"]
print(lista)
indice = int(input("Indice: "))

qtd_elementos = len(lista)
if indice > qtd_elementos or indice < 0:
    print("Indice inexistente!")
else:
    elem = lista.pop(indice)
    print(f"O elemento {elem} foi removido!")

print(lista)
'''

#Remover pelo conteudo 
'''
#          0      1    2    3    4         5
lista = ["fiap", 65, True, 25, 68.8, "Engenharia"]
lista_aux = []
for elem in lista:
    lista_aux.append(str(elem))
print(lista_aux)
elem = input("Elemento: ")
qtd = lista_aux.count(elem)

if qtd > 0:
    indice = lista_aux.index(elem)
    lista.pop(indice)
    print("Item removido!")
else:
    print("Elemento não encontrado")

print(lista)
'''