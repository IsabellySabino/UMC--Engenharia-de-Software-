n = int(input('Insira um número: '))
anterior = 0
atual = 1
contador = 0


while contador < n:
    print(atual, end=' ')
    soma = anterior + atual
    anterior = atual 
    atual = soma
    contador += 1