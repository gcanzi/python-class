import os
os.system("cls")

# metodos para strings
#        0123456789012345678901234567890123456789012345678901
frase = "Veremos agora como funciona o fatiamento com strings"
print(frase.find("agora")) # mostra a partir de qual posição encontrou a palavra
# o .find, procura em algum lugar o que foi especificado e retorna a posição do que for encontrado
print(frase.find("m"))
print(frase.find("fiap")) # retorna -1, pois não foi encontrado 
print(frase.find("o"))
print(frase.find("o", 10, 20)) # começa contando a partir do 10 até o 20

nome = ["Gustavo", "Moretim", "Canzi"]
print(nome)
print(" ".join(nome))
# .join(), gera uma string a partir de uma lista de string

nomeStr = " ".join(nome)
print(nome, nomeStr)

nomeStr = "".join(nome) # fica tudo junto
print(nome, nomeStr)

nomeStr = "-".join(nome)
print(nome, nomeStr)

# split
# .split(), separa o texto com o que for colocado no ()
nome2 = "Gustavo Moretim Canzi"
print(nome2)
print(nome2.split())
print(nome2.split(), "tem", len(nome2.split()), "palavras")
print(nome2.split('e'))

# replace
nome1 = nome.replace('e', 'E')
print(nome1)