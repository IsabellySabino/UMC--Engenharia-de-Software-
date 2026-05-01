vetor= []

for i in range(10):
    print("Aluno", i + 1)
    soma = 0

    for a in range(4):
        nota = float(input("Qual a sua nota: "))
        soma += nota
    
    media = soma/4

    vetor.append(media)

aprovados = 0

for media in vetor:
    if media >= 7:
         aprovados += 1

print("Quantidade de alunos com média maior ou igual a 7 é: ", aprovados)
    
    