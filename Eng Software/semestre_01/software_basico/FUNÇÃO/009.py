def tabuada(n):
    contador = 1
    while contador <= 10 :
        multi = n * contador
        print(f'{n} x {contador} = {multi}')
        contador = contador +1


n = int (input('Digite um número: '))
resultado = tabuada(n)