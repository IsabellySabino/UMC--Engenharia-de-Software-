n1= float(input("Insira o primeiro número: "))
n2= float(input("Insira o segundo número: "))
n3= float(input("Insira o terceiro número: "))
n4= float(input("Insira o quarta número: "))
n5= float(input("Insira o quinto número: "))
num= max(n1,n2,n3,n4,n5)
if n1 == n2 == n3 == n4 == n5:
    print("Todos os números são iguais")

elif n1==n2 or n1 == n3 or n1 == n4 or n1 == n5 or n2 == n3 or n2 == n4 or n2 == n5 or n3 == n4 or n3 == n5 or n4 == n5:
    print(f"existem dois ou mais numeros iguais, mas o maior é {num}")

else:
    print(f"O maior numero é o {num}")
