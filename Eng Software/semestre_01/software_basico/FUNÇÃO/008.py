def maioridade(idade):
    if idade < 0: 
        print('Idade inválida')
        
    elif idade >= 18:  
        print('Maior de idade')
        
    else:
        print('Menor de idade')

    return idade

    
idade = int(input('Digite sua idade: '))
resultado = maioridade(idade)
