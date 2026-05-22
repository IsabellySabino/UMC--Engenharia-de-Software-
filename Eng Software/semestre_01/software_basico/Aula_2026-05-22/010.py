numeros = []
par = []
impar = []

n = 1

while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        numeros.append(n)

        if n % 2 == 0:
            par.append(n)
    
        elif n % 2 == 1: 
            impar.append(n)

if len(numeros) > 0:
    maior =max(numeros)
    menor = min(numeros)
    
    print(f'Os números são {numeros}\nOs números pares são {par}\nOs números ímpares são {impar}\nO número maior é {maior}\nO número menor é {menor} ') 
else:
    print('Nenhum número foi digitado')