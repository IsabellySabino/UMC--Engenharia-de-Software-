v_hora= float(input("Insirao o valor das horas trabalhadas: "))
q_hora= float(input("Insira a quantidade de horas trabalhadas: "))

s_bruto= v_hora * q_hora

# processamento do desconto do imposto de renda
if s_bruto<=900:
    ir = 0
    d_ir = 0

elif s_bruto > 900  and s_bruto <= 1500:
    ir= 5
    d_ir= s_bruto * 0.05

elif s_bruto > 1500 and s_bruto <= 2500:
    ir=10
    d_ir = s_bruto * 0.10

else:
    ir= 20
    d_ir = s_bruto * 0.20

# no exemplo do professor não foi utilizado o desconto do sindicato, mas como estava lá como informação eu utilizei
v_sind = 3
sindicato = s_bruto * v_sind/100

# utilizei v_inss= 10 ao invés de 0.10 para não usar a formúla apenas para mostrar o valor
v_inss= 10
inss = s_bruto * v_inss/100

v_fgts= 11
fgts= s_bruto * v_fgts/100

descontos= d_ir + sindicato + inss

s_liquido = s_bruto - descontos

print(f"Salário Bruto: ({v_hora}*{q_hora}): R$", s_bruto)
print(f"(-) IR ({ir}%):                R$", d_ir)
print(f"(-) INSS ({v_inss}%):              R$", inss)
print(f"(-) Sindicato ({v_sind}%):          R$", sindicato)
print(f"FGTS ({v_fgts}%):                  R$", fgts)
print("Total de descontos:          R$", descontos)
print("Salário Líquido:             R$", s_liquido)