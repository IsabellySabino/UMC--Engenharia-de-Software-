estoque = 1000
historico = []

sessao_ativa = True

print("--- Bem-vindo ao Caixa Eletrônico ---")

while sessao_ativa:
    n = input('O usuário deseja  1) Saque, 2) Depósito, 3) Extrato, 4) Sair: ')

    if n == '1':
        valor = float(input('Digite qual valor você quer sacar: '))
        if valor >= estoque :
            print('Erro: Saldo insuficiente.')
        else:
            estoque -= valor 
            historico.append(valor)
            print('Estoque atual: ', estoque)

    elif n == '2':
        valor_d = float(input('Digite qual o valor que você quer depositar: '))
        estoque += valor_d
        historico.append(valor_d)
        print('Estoque atual: ', estoque)

    elif n == '3':
        for transacao in historico:
            print(transacao)
            print('Estoque atual: ', estoque)
        
        if not historico:
            print('Não tem nenhuma transação')

    elif n == '4':
        print('Programa encerrado')
        sesao_desativada = False
        break
    
    else: 
        print('Opção inválida. Tente novamente')