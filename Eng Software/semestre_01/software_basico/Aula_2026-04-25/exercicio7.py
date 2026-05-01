vetor=[]
soma = 0

for i in range(5):
    num = float(input("Digite um número: "))
    vetor.append(num)

soma += sum(vetor)
media = soma/5

print(soma)
print(media)
print(vetor)

