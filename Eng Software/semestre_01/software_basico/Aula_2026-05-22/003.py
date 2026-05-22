numeros = []

for i in range(1, 6):
    n = int(input('Digite um número inteiro: '))
    numeros.append(n)

maior = max(numeros)
menor = min(numeros)

print(f'Os valores são {numeros}\nO maior valor é {maior}\nO menor valor é {menor}')
