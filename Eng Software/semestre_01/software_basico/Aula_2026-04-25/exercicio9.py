a = []
soma = 0

for i in range(10):
    num = int(input("Digite um número: "))
    a.append(num)

for valor in a:
     soma =soma + (valor**2)

print(soma)