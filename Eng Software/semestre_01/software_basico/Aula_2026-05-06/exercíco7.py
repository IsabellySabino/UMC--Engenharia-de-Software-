def valor_pagamento(valor, dia):
    if dia == 0:
        # aqui não utilizei nanhuma conta, pois não tem o porque cobrar juros e apenas retornei o valor já adicionado
        return valor
    else:
        valor_f = valor + (valor * 0.03) + (valor * (0.001*dia))
        return valor_f
# criei essas duas váriaveis zeradas para adicionar no meio do programa os valores
qtd = 0
valor_t = 0

# utilizei while para criar um looping 
while True:
    valor_p = float(input("Digite o  valor da prestação: "))

    if valor_p == 0:
        break 


    dias_a = int(input('Digite o número de dias atrasados: '))

# chamei a função para adicionar valor da prestaçãoe em valor e dias de atrado em dia
    resultado = valor_pagamento(valor_p, dias_a)

    print(f"Valor total da prestação é: {resultado:.2f} ")

    qtd += 1
    valor_t += resultado


# utilizei :.2f para mostrar apenas duas casas decimais, assim como eu fiz a cima 
print(f"Relátorio do dia:\nQuantidade de prestações:{qtd}\nValor total pago:{valor_t:.2f}",)

