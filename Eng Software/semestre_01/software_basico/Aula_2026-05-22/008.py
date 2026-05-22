matriz = [
    [10, 12, 13],
    [10, 12, 13],
    [10, 12, 13]
]


maior_10= 0

for linha in matriz:    
    print(linha)

    for numeros in linha:
        if numeros > 10:
            maior_10+= 1

print('A quantidade núemros maior que 10 é', maior_10)