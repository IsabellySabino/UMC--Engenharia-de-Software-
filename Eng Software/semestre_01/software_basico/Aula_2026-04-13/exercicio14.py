peso = float(input("Qual o peso do peixe? "))
limite = 50

if peso > 50:
    excesso = peso - limite
    multa = excesso * 4

else:
    excesso = 0
    multa = 0

print("O excesso é: ", excesso)
print("O valo da multa é: ", multa)
