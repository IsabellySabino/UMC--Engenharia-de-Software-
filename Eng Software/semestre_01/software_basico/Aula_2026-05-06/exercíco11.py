def converter(data_s):

    dia, mes, ano = data_s.split("/")

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    if dia <1 or dia>31 or mes <1 or mes >12:
        return None

        
    if mes in [4, 6 , 9, 11] and dia > 30:
            return None 
    
    if  mes == 2 and dia > 28:
         return None
        
    else:
        extenso = meses [mes -1]
        return f"{dia} de {extenso} de {ano}"


data = input("Digite a data (dd/mm/aaaa): ")
resultado = converter(data)

if resultado: 
     print(resultado)

else:
    print("Data inválida")