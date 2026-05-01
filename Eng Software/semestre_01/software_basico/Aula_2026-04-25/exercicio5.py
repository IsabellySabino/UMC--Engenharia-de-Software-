vetor = []
par = []
impares = []

for i in range (20):
    num = int(input("Digite um número: "))
    vetor.append(num)

    if num % 2 != 0:
        impares.append(num)
        

    else:
        par.append(num)
    

print(vetor)
print(par)
print(impares)