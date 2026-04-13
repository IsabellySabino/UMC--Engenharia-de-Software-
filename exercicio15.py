valor_hora= float(input("Quanto você ganha por hora? "))
numero_horas= float(input("Números de horas trabalhadas por mês? "))

salario_bruto= valor_hora*numero_horas

inss= salario_bruto*8/100
sindicato = salario_bruto * 5/100
ir = salario_bruto * 11 / 100

salario_liquido= salario_bruto- inss - sindicato - ir

print ("O salário bruto é: R$", salario_bruto)
print ("Valor pago ao Inss é: R$", inss)
print ("Valor pago ao sindicato é: R$", sindicato)
print ("Valor pago ao IR é: R$", ir)
print ("O Salário líquido é: R$", salario_liquido)