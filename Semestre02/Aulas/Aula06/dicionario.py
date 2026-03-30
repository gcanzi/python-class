import os
os.system('cls')

aluno = {
    "nome": "Gustavo",
    "idade": 22,
    "curso": "ES",
}

print(aluno)

if aluno["nome"] == "Gustavo": print("Ok!")
aluno["idade"] = int (input("Idade:"))
print(aluno.get("curso"))
print(aluno.get("nota")) # como não existe essa key, não retorna nada, porem não da erro
# print(aluno["nota"]) -> dessa forma vai dar erro