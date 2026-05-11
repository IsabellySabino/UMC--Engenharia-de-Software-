nome = input("Digite seu nome: ").upper()
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

if nome == "" or idade < 16 or idade > 60 or altura < 1.0 or altura > 2.5:
    print('Dados inválidos, não matriculado')

else:
    print('Dados válidos')
    print(nome)
    print(idade)
    print(altura)
    print('Aluno matrículado')