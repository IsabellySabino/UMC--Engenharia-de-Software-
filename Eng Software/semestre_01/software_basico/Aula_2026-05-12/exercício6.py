while True:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite o segundo número: '))

    if n1 > 10 or n2 > 10:
        print('Nota inválida, digite novamente ')
        continue

    media = (n1+n2) / 2
    print(f'A média é {media}')

    opcao = input('Deseja calcular outra média? (S- sim ou N-não)').upper()
    
    while opcao != 'S' and opcao != 'N':
            print('Opção inválida! Digite novamente')
            opcao = input('Deseja calcular outra média? (S- sim ou N-não)').upper()
        
    if opcao == 'N':
        print('Programa encerrado')
        break
