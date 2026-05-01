vetor = []
consoantes = ["B", 'C', "D", 'F', "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

for i in range(10):
    carac = input('Digite um caractere: ').upper()
    
    if carac in consoantes:
        vetor.append(carac)

print(f"Quantidade de consoantes: {len(vetor)}")
print(f"Consoantes lidas: {vetor}")