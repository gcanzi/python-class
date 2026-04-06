import os
os.system("cls")
# os.sytem("cls" if os.name == "nt" else "clear") -> assim funciona em qualquer sistema operacional

idade = 12
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

print("Maior de idade") if idade >= 18 else print("Menor de idade")

# Atribuindo valor a um variavel

salario = 1000
bonus = 300

inss =  salario * 0.1 if salario > 5000 else salario * 0.05
print(salario, inss)

salarioLiq = salario - (salario * 0.1 if salario > 5000 else salario * 0.05) + bonus
print(salario, inss, salarioLiq)