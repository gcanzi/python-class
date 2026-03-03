# Definição da função - sem parametros
def valorDePi():
    return 3.14159

#dado um numero por parametro, faça uma função que retorne o proximo numero
def proximoNumero(n):
    return n + 1

# Uso
raio = float(input("Digite o raio: "))
area_circulo = valorDePi() * raio ** 2
print(f"Área do circulo com raio {raio} é {area_circulo}")

numero = int(input("Numero: "))
prox = proximoNumero(numero)
print(f"{numero}, próximo {prox}")