while True:
    try:
        n1= int(input("Insira um número inteiro: "))
        if n1 <=0:
            print("\nPor favor, digite um número inteiro positivo!")
 
        primo=True
 
        if n1 ==1:
            primo = False
       
        else:
            for i in range(2, int(n1**0.5)+1):
                if n1%i == 0:
                    primo=False
                    break
 
        if primo:
            print(f"\n{n1} é um número primo.")
       
        else:
            print(f"\n{n1} não é um número primo.")
   
    except ValueError:
        print("\nEntrada inválida. Digite apenas números inteiros por gentileza.")
        continue
 
    continuar= input("\nDeseja verificar outro número? (S/N)").upper()
    if continuar != 'S':
        print("\nPrograma encerrado.")
        break