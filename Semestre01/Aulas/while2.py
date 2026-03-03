nota = int(input("Digite uma nota válida entre 0 e 10 = "))

while nota < 0 or nota > 10:
    print("Nota inválida, digite novamente:")
    nota = int(input("Digite uma nota válida entre 0 e 10 = "))
    print(f"Sua nota foi {nota}")
    
