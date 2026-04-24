area = float(input("Digite a área em m² a ser pintada: "))

cobertura = area/3
import math
latas_tinta = math.ceil(cobertura / 18)

preço_total = latas_tinta*80

print("A quantidade de latas é ", latas_tinta)
print("O preço total é: R$", preço_total)
