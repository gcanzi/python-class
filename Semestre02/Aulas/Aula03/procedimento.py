# ---------- CRIAÇÃO DOS MÓDULOS    
# ----- Procedimentos

# sem parametros (argumentos)
def saudacao1():
    print("Seja bem-vindo!")

# com parametros (argumentos)
def saudacao2(nome):
    print(f"Seja bem-vindo {nome}!")

# com parametros (argumentos)
def saudacao3(nome, hora):
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"

    print(f"{msg}, seja bem-vindo {nome}!")

# ---------- PROGRAMA PRINCIPAL
import os
os.system("cls")

saudacao1()
saudacao2("Canzi")
saudacao3("Canzi", 17)