# Utilizando SOMENTE os métodos apresentados nesta apresentação, faça um subalgoritmo de nome vogal_maiuscula(string) que passe uma string por parâmetro e retorne-a com as vogais convertidas em maiúsculas.

def vogal_maiuscula(f: str) -> str:
    f = f.replace('a','A')
    f = f.replace('e','E')
    f = f.replace('i','I')
    f = f.replace('o','O')
    f = f.replace('u','U')
    return f