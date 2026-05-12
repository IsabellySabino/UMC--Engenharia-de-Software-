r = float(input('Digite o valor de r (número real): '))
n = int(input('Digite o valo de n (número inteiro): '))

soma = 0 
i = 0
termos = []

while i<= n:
    potencia = r**i 
    soma += potencia
    termos.append(str(potencia))

    i += 1

sequencia = "+".join(termos)
print(f"\nS_{n} = {sequencia} = {soma:.3f}")