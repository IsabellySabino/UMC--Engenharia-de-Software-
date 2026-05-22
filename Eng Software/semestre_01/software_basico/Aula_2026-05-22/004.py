matriz = [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]
]

soma_d = 0

for i in range(len(matriz)):
    soma_d += matriz[i][i]

for linha in matriz:    
    print(linha)

print('A soma da diagonal principal é:', soma_d)