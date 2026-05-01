vetor1 = []
vetor2 = []
vetor3 = []

for i in range(2):
    num = float(input("Digite um número: "))
    vetor1.append(num)

for i in range(2):
    num = float(input("Digite um número: "))
    vetor2.append(num)
        
for i in range(2):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(vetor1)
print(vetor2)
print(vetor3)