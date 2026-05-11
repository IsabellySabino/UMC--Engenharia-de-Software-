def num(valor):
    if valor > 0:
        # pedir para ele retornar P se fosse um número positivo 
        return ("P")
    else:
        # pedi para ele retornar N se fosse um número NEGATIVO
        return ("N")
    
n = float(input("Digite um valor: "))

# adicionei numero = n a função num
resultado = num(n)


print(f"O VALOR {n} é {resultado} ")
