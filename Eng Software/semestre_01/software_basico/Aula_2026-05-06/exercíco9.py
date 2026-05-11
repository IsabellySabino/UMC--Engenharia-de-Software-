def retorne (reverso):
    texto=str(reverso)
    invertido = texto [::-1]
    return invertido

numero= int(input("Digite um número: "))

resultado = retorne(numero)

print(resultado)


