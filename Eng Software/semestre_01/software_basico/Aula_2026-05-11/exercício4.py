notas = []

for i in range(5):
    nota= float(input(f'Insira a {i+1} nota: '))
    notas.append(nota)
    media = sum(notas)/len(notas)
    
    maior= max(notas)
    menor= min(notas)

    aprovados = 0
    for n in notas:
        if n >= 6:
            aprovados += 1

print('Média da turma: ', media)
print('Maior nota: ', maior)
print('Menor nota: ', menor)
print('Total de alunos aprovados: ', aprovados)
