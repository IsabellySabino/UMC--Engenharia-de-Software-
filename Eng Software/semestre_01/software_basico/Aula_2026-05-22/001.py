positivos = 0
negativos = 0

for i in range(1,11):
    n = int(input(f'Digite o {i}° número: '))
    
    if n > 0:
        positivos +=1
    
    elif n < 0:
        negativos += 1
    
print(f'Os números negativos são {negativos}')
print(f'Os números positivos são {positivos}')