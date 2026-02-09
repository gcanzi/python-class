import random

numero_sorteado = random.randint(1, 10)

cont = 0

while cont < 3:
    numero = int(input("Advinhe qual numero estou pensando? (Entre 1 e 10, 0 para desistir.)"))
    cont = cont + 1

    if numero ==0:
        print("Você desistiu do jogo!")
        break
    elif numero == numero_sorteado:
        print(f"Parabens você acertou em {cont} tentativas!")
        break
    elif cont == 3:
        print(f"Acabou suas tentativas. O numero correto é {numero_sorteado}")
        break
    else:
        print("Errou, tente novamente")
