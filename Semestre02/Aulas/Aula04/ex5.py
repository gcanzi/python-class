# Crie uma função chamada maior_numero(lista) que receba uma lista de números como parâmetro e retorne o maior valor encontrado.
# No programa principal, crie uma lista com vários números e mostre o maior valor.

lista = []

def preencherLista(l: list) -> None:
    while True:
        elem = input("Elemento: ")
        if elem != '.':
            l.append(float(elem))
        else:
            break

preencherLista(lista)

def maiorNumero(l: list) -> float:
    maior = l[0]
    for i in range(1, len(l)):
        if l[i] > maior:
            maior = l[i]
    return maior

# chama a função criada para ver o maior
print(f"O maior numero da lista é {maiorNumero(lista)}")

# utiliza da linguagem para fazer a mesma função
print(f"O maior numero da lista é {max(lista)}")