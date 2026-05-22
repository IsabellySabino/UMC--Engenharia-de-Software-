nomes = []
alunos = {}
nome_a = []
nota_a = []

while True:
    nome = input('Digite seu nome: ')
    if nome.lower() == 'fim':
        break
    
    notas = float(input('Digite sua nota: '))
    
    nomes.append(nome)
    alunos[nome] = {'nota': notas}
    if notas >= 7:
        nome_a.append(nome)
        nota_a.append(notas)


print(nomes)
print(f'Os alunos aprovados foram {nome_a} e suas notas foram {nota_a}')
