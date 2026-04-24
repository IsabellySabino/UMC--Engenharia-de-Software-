data = input("Digite uma data (dd/mm/aaaa): ")

#  vou separar a data em 3 partes usando .split()
dia, mes, ano = data.split("/")

# depois vou converter o texto para número inteiro
dia = int(dia)
mes = int(mes)
ano = int(ano)

valida = True

if mes < 1 or mes > 12:
    valida = False

elif dia < 1 or dia > 31:
    valida = False

    # processar meses com 30 dias e fevereiro
elif mes in [1, 3, 5, 7, 8 , 10, 12]:
    if dia > 31:
        valida = False
        
elif mes in [4, 6 , 9, 11]:
        if dia>30 :
             valido = False

# aqui vai verificar se o ano é bissexto ou não
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if dia>29:
               valida = False
            
    else:
        if dia > 28:
            valida =False

if valida:
     print ("Data válida")

else: 
     print ("Data inválida")


            
