import os
os.system("cls")

# o string(str) é uma lista e conta por posição tambem 

#        0123456789012345678901234567890123456789012345678901
frase = "Agora veremos como funciona o fatiamento com strings"
print(frase)
print(frase[4]) # chama a posição do caractere no texto

for carac in frase: # adiciona um espaço em cada posição da string
    print(carac, end=" ")

print()
print(frase[7:15]) # ex de fatiamento
print(frase[2:30:2])
print(frase[::-1])
