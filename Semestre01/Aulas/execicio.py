# Dado um número, exibir a tabuada correspondente ( faça uma versão para o pré-condicional e outra para o pós-condicional).

numero = int(input("Digite qualquer número para saber a tabuada dele: "))
cont = 0

while cont < 10:
    cont = cont + 1
    resultado = numero * cont
    print(f"{numero} X {cont} = {resultado}")
