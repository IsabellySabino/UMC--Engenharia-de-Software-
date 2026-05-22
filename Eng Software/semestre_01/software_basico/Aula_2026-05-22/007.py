numeros = []
par = []
n = 0

while n != -1:
    n = int(input('Digite um número inteiro: '))
    if n != -1:
        numeros.append(n)
        if n % 2 == 0:
            par.append(n)

print('Os números são: ',numeros )
print('Os números pares são: ',par )