n = int(input('Digite um número: '))
primo = True

if n <= 1:
    primo=False

else:
    for divisor in range(2, n):
        if n % divisor == 0:
            primo = False
            break
    
if primo:
    print('Número primo')

else:
    print('Esse número não é primo')