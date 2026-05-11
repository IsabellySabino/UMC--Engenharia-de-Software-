import random

def embaralha(palavra):
    sorteio =random.sample(palavra, len(palavra))

    resultado = "".join(sorteio)
    return resultado

texto = input("Digite uma palavra: ").upper()
sorteio= embaralha(texto)


print(f"A palavra embaralhada é : ", sorteio)