import os
os.system('cls')

def isfloat(v: str) -> bool:
    if v[0] == '-':
        v = v.replace('-', '', 1)
    if v[0] == '+':
        v = v.replace('+', '', 1)
    v = v.replace('.', '', 1)
    return v.isdigit()

# uso
valor = "345"
print(isfloat(valor), valor) # True
valor = "-345"
print(isfloat(valor), valor) # True
valor = "-AB345"
print(isfloat(valor), valor) # False
valor = "-345.1"
print(isfloat(valor), valor) # True
valor = "+345"
print(isfloat(valor), valor) # True
valor = "-34+5"
print(isfloat(valor), valor) # False
valor = "+34-5"
print(isfloat(valor), valor) # False