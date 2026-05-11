import random 

dado1 = random.randint(1, 6)
dado2= random.randint(1, 6)
soma= dado1+dado2

print(soma)

if soma == 7 or soma == 11:
    print("NATURAL, você ganhou a primeira rodada")

elif soma == 2 or soma == 3 or soma == 12:
    print("CAPS, você perdeu")

else:
    ponto=soma
    print("PONTO: ", ponto)

    while True:

        dado1 = random.randint(1, 6)
        dado2= random.randint(1, 6)
        soma= dado1+dado2

        print(soma)

        if soma == ponto:
            print("VOCÊ GANHOU")
            break

        elif soma == 7:
            print("VOCÊ PERDEU")
            break

        else:
            continue