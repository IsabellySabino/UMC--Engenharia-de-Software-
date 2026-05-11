n = int(input('Digite um número: '))

soma = 0
for i in range(n):
    n2= int(input('Digite um valor: '))
    soma += n2
    media = soma/n

print(f'A média é {media}')