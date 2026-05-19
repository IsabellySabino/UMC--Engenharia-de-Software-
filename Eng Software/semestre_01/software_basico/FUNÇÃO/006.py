def desconto(valor):
    desconto = valor * (15/100)
    v_final = valor - desconto 
    print(f'O valor do produto é {valor} e com o desconto fica {v_final:.2f}')
    return v_final

valor = float(input('Insira o valor do produto: '))
resultado = desconto(valor)