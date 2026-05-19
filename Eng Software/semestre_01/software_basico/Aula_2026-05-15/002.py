matriz = [
    [5, 8],
    [3, 10]
]

soma = sum(sum(linha) for linha in matriz)


for linha in matriz:
    print(linha)

print('A soma dos elementos é:', soma)