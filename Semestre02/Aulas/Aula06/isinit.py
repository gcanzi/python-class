def isint(v: str) -> bool:
    if v[0] == '-':
        v = v.replace('-', '', 1)
    if v[0] == '+':
        v = v.replace('+', '', 1)
    return v.isdigit()

# uso
valor = "345"
print(isint(valor), valor) # True
valor = "-345"
print(isint(valor), valor) # True
valor = "-AB345"
print(isint(valor), valor) # False
valor = "-345.1"
print(isint(valor), valor) # False
valor = "+345"
print(isint(valor), valor) # True
valor = "-34+5"
print(isint(valor), valor) # False
valor = "+34-5"
print(isint(valor), valor) # False

