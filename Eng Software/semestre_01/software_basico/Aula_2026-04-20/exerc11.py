salario = float(input("Insira o valor do Salário atual: "))

if salario <= 280:
    percentual = 20
    aumento = salario * 0.20
    novo_salario = salario + aumento

elif salario>280 and salario <= 700:
    percentual = 15
    aumento = salario * 0.15
    novo_salario = salario + aumento

elif salario>700 and salario<=1500:
    percentual = 10
    aumento = salario * 0.10
    novo_salario = salario + aumento
  
else:
    percentual = 5
    aumento = salario * 0.05
    novo_salario = salario + aumento

print (f"O salario atual é R$ {salario}\nO percentual aplicado é de {percentual}%\nO valor do aumento é R${aumento}\nO novo salário é R${novo_salario}")