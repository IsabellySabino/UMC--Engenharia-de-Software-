def somar_tres(a, b, c):
    # retornei a, b e c para somar e dar o resultado 
    return a + b + c

valores = []

for i in range (3):
    num = float(input("Digite um valor: "))
    # adicionei numeros na lista valores
    valores.append(num)
    
# cahmei a função somar tres e coloquei valores[0] para a, valores [1] para b e valores[2] para c 
soma = somar_tres(valores[0], valores [1], valores [2])
    
print(f"SOMANDO OS VALORES {valores} TEMOS {soma}")