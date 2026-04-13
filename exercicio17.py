import math

area = float(input("Digite a área em m² a ser pintada: "))
area_folga = area * 1.10

cobertura = area_folga / 6

latas_tinta = math.ceil(cobertura / 18)
preço_tinta = latas_tinta * 80

galoes_so = math.ceil(cobertura/3.6)
preço_galao = galoes_so * 25

latas = int(cobertura//18)
resto = cobertura - (latas * 18)

galoes = math.ceil(resto / 3.6)

preço_mistura = (latas * 80) + (galoes * 25)

print("A quantidade de latas é ", latas_tinta,
      " e o  valor em latas é: R$", preço_tinta)
print("A quantidade de Galões é ", galoes_so,
      " e o  valor em galões é: R$", preço_galao)
print("A quantidade de Latas e Galões é ", latas, "e",
      galoes, " e o valor da mistura é: R$", preço_mistura)
