while True:
    operacao = input('Qual operação você quer realizar? (A - adição, S - subtração, D - divisão, M - multiplicação e E - exist para sair)').upper()

    if operacao == 'E':
        print('Progrma encerrado')
        break 

    elif operacao == 'A':
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        soma = n1 + n2
        print('A soma é: ', soma)

    elif operacao == 'S':
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        sub = n1 - n2 
        print('A subtração é: ', sub)

    elif operacao == 'D':
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        if n1 == 0 or n2 == 0:
            print('Número inválido')
            continue
        div = n1 / n2 
        print('A divisão é: ', div)

    elif operacao == 'M':
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        multi = n1 * n2 
        print('A multiplicação é: ', multi)

    else:
        print('Opção inválida')
        continue