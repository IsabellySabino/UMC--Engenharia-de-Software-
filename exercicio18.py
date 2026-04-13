MB= float(input("Insira o tamanho do arquivo para download em MB: "))
Mbps= float(input("Insira a velocidade de um link da internet em Mbps: "))

arquivo_megabits= MB * 8
segundos = arquivo_megabits / Mbps
minutos= segundos / 60

print("O tempo aproximado de download do arquivo é: ", minutos)