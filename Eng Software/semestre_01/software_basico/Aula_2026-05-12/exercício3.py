n = int(input('Digite um número: '))
primo = True

if n <= 1:
    primo=False

else:
    divisor = 2 
    while divisor < n:
        if n % divisor == 0:
            primo = False
            break

        divisor +=1
    
if primo:
    print('Número primo')

else:
    print('Esse número não é primo')