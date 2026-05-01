idade = []
altura = []

for i in range(5):
    print("Pessoas", i+1)

    idade_p = int(input('Idade: '))
    altura_p = float(input("Altura: "))

    idade.append(idade_p)
    altura.append(altura_p)

idade.reverse()
altura.reverse()

for i in range(len(idade)):
    print("\nPessoa", i + 1)
    print("Idade:", idade[i])
    print("Altura:", altura[i])
