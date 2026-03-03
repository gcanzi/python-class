# EXEMPLO
# Exibir os numeros de 1 a 10.

# laço pré-condicional - enquanto - while <condicao>
# Situações 0,N. Analisa primeiro depois executa uma ação
print("Com o while")
volta = 1
while volta <= 10:
    print(volta)
    volta = volta + 1

# laço pós-condicional - repita - while while True
# Situações 0,N. Executa uma ação depois analisa
print("Com o while True")
volta = 0
while True:
    print(volta)
    volta = volta + 1
    if volta > 10: break

# laço contador - para - for
# situações onde o numero de voltas é previsivel
print("Com o For")
for i in range (1,11,1):
    print(volta)

print("Com o For")
for i in range (5,21,3):
    print(volta)

