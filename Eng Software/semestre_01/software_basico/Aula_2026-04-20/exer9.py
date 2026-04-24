n1= float(input("Insira um número: "))
n2= float (input("Insira outro número: "))
n3= float(input("Insira outro número: "))

if n1>n2 and n1>n3:
    maior = n1
    if n2>=n3:
        meio = n2
        menor = n3
    else: 
        meio = n3
        menor = n2

elif n2>=1 and n2>=n3:
    maior = n2
    if n1>=n3:
        meio= n1
        menor=n3
    else:
        meio= n3
        menor= n1
else:
    maior = n3
    if n1>=n2:
        meio = n1 
        menor = n2
    else:
        meio = n2
        menor = n1

print (maior, meio, menor)