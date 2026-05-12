n = int(input('Digite um número: '))
soma = 0
i = 0

while i < n:
    n2= int(input('Digite um valor: '))
    soma += n2
    i += 1

if n > 0:
    media = soma/n
    print(f'A média é {media}')

else:
    print("Não é possível calcular a média de 0 números.")