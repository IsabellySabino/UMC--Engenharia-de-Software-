aluno = {}

maior =-1
nome_maior= ""

for i in range(1,4):
    print(f'---CADASTRO DO {i}° ALUNO---')
    nome = input('Digite seu nome: ')
    nota = float(input('Digite sua nota: '))

    aluno[nome] = {'nota': nota}

    if nota > maior:
        maior = nota
        nome_maior = nome 
    
print(f'O aluno com a nota maior é a/o {nome_maior}\nA nota é {maior}')