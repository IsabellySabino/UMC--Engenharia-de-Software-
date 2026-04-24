while True:
    
    try:
        nota=float(input("Insira sua nota:  "))
        if 0<=nota<=10:
            print("Nota válida!")
            break
        else:
            print("Nota inválida! A nota deve ser um número entre 0 à 10, tente novamente.")
    
    except ValueError:
        print("Entrada inválida! Por favor digite um número")
    
 




