def digitos(n):
    # utilizei abs para usar o valor absoluto de um número
    n = abs(n)
    texto = str(n)
    return len(texto)
    

numero =int(input("Dgite um número: "))

resultado =digitos(numero)

print(resultado)