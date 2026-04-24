n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite outro número: "))

# processando qual número é maior

if n1 > n2 and n1 > n3:
    print(f"{n1} é o número maior")

elif n2 > n1 and n2 > n3:
    print(f"{n2} é o número maior")

else:
    print(f"{n3} é o número maior")

# processando qual número é o menor

if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor número")

elif n2 < n1 and n2 < n3:
    print(f"{n2} é o menor número")

else:
    print(f"{n3} é o menor número")
