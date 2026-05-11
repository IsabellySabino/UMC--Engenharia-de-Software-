def tempo(hora, minuto):
    if hora <= 11:
        periodo = "A.M"
    
    else:
        periodo = "P.M"

# criei esse if para converter a hora se ela fosse maior que 12 
    if hora > 12:
        hora = hora - 12
        # criei esse retorno porque se não ele não me retorna o resultado
    return hora, minuto, periodo

hora = int(input("Digite somente a hora: "))
minuto= int(input("Digite somente os minutos: "))

# criei essa variavel para mostra as horas, os minutos e o periodo, e também adicionar hora e minuto na fnção tempo
h, m, p= tempo(hora, minuto)

print(f"Horas: ", h,m,p)


