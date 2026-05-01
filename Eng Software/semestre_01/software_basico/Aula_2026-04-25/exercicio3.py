vetor = []

for i in range (4):
    nota = float(input("Digite a nota: "))
    vetor.append(nota)

media = sum(vetor)/4

print(f"As notas são: {vetor}\nA média é: {media}")
