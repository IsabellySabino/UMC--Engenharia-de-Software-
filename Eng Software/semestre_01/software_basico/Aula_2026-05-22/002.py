soma = 0
contador = 0
n = - 1


while n != 0:
    n = float(input('Digite um número: '))
    if n != 0:
        soma += n
        contador += 1

if contador > 0:    
    media = soma / contador 
    print(soma, media)

else:
    print('Nenhum número válido foi digitado')