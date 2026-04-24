n1= int(input("Digite um número inteiro menor que 1000: "))

if n1 < 1000 and n1 >= 0:
    centenas = n1 // 100
    resto = n1 % 100
   
    dezenas = resto // 10
    
    unidades = n1 % 10
    
    partes = []

    if centenas > 0:
        if centenas == 1:
            partes.append("1 centena")
        
        else:
            partes.append(f"{centenas} centenas")
        
    if dezenas > 0:
        if dezenas ==1:
            partes.append("1 dezena")
        
        else:
            partes.append(f"{dezenas} dezenas ")
        
    if unidades > 0:
        if unidades == 1:
            partes.append("1 unidade")
        
        else:
            partes.append(f"{unidades} unidades")
    
    if len(partes) == 1:
        frase = partes [0]
    
    elif len (partes) ==2:
        frase = partes[0] + " e " + partes [1]
    
    else:
        frase = partes [0] + ", " + partes [1] + " e " + partes[2]
    
    print(f"{n1} = {frase}")

else:
    print ("Número inválido")