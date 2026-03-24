# Dada uma lista e um caractere por parâmetro, faça uma função que retorne em uma lista com os indices onde os caracteres foram encontrados.

def retorna_indices(f: str, c: str) -> list:
    inicio = 0
    fim = len(f)
    lista_indice = list()
    while True:
        indice = f.find(c,inicio,fim)  # 1
        if indice == -1:
            break
        else:
            lista_indice.append(indice)
            inicio = indice + 1
            # indice = f.find(c,inicio,fim)

    return lista_indice

frase = "banana"
lista = retorna_indices(frase, 'a')
print(lista)