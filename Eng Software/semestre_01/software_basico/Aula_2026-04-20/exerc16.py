a = float(input("Insira o valor de a: "))
if a == 0:
    print("Não é uma equação de segundo grau")
    exit()

b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = (b**2 - 4*a*c)

if delta < 0:
    print("A equação não possui raízes reais")

elif delta == 0:
    x = (-b + delta**0.5) / (2*a)
    print("Possui uma raiz real")
    print("Valor de x: {: .2f}".format(x))

else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("Possui duas raízes reais")
    print("\nValor de x1: {0: .2f}".format(x1))
    print("\nValor do x2: {0: .2f}".format(x2))
