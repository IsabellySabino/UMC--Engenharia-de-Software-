l1= float(input("Insira o primeiro lado do triângulo: "))
l2= float(input("Insira o segundo lado do triângulo: "))
l3= float(input("Insira o terceiro lado do triângulo: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Os valores inseridos correspondem a um triângulo")
    
    if l1 == l2 and l2 == l3:
        print("Triângulo equiilátero")
    
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo isósceles")
    
    else: 
        print("Triângulo escaleno ")
else:
    print("Os valores inseridos não formam um triângulo")

