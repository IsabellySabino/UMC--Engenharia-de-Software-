turno = input("Insira qual turno você estuda M - Matutino, V - Vesperino e N - Noturno: ").upper()



if turno == "M":
    print("Bom dia!")

elif turno == "V":
    print("Boa tarde!")

elif turno == "N":
    print("Boa noite!")

else:
    print("Valor inválido")
