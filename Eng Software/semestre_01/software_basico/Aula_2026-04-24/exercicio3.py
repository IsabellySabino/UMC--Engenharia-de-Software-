#validação de nome
while True:

    nome = input("Insira o nome: ")
   
    if len(nome) <= 3:
        print("Nome precisa ter mais do que 3 caracteres")
        continue

    idade = int(input("Insira a idade: "))

    if idade <= 0 or idade > 150:
        print("Idade inválida")
        continue
    
    salario = float(input("Informe o seu salario: "))

    if salario == 0:
        print("Salário inválido")
        continue

    estado_civil = input("Insira o seu estado civil:\nS-Solteiro\nC-Casado\nV - Viúvo\nD - Divorciado\n").upper()
    if estado_civil not in ["S", "C", "V", "D"]:
        print("Estado civil inválido, tente novamente.")
        continue
    break



