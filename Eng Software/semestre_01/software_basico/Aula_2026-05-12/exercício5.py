n = int(input('Digite um valor: '))
contador = 1
print()
print(f'{'TABUADA':=^20}')
print()

while contador <= 10:
    resultado = n * contador 
    print(f'{n} x {contador} = {resultado}')
    contador +=1