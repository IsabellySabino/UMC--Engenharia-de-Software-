def area(base, altura):
     print(f'A área é igual a {base} x {altura} = {base * altura}')
     return base * altura 


base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))

resultado = area(base, altura)
areas = resultado
print(resultado)