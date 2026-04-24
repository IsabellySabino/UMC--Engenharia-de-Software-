ano= float(input("Insira um ano: "))

# verificando se o ano é divisível por 4 e por 400
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Este ano é bissexto.")
else:
    print("Este ano não é bissexto.")


