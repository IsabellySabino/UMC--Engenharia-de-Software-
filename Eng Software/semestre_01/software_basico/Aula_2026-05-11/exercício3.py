estoque = 100

while True:
    print(f"\nEstoque atual:{estoque}\n")
    opcao = input("O usuário deseja adicionar (a), remover(r) ou sair (s)? ").lower()


    if opcao == "a":
        n = float(input("Digite a quantidade que você quer adicionar: "))
        estoque += n
    
    elif opcao == "r":
            print(f"\nEstoque atual:{estoque}\n")
            n = float(input("Digite a quantidade que você quer tirar: "))
            
            if n > estoque :
                print("Erro: estoque não pode ficar negativo")

            else: 
                estoque -= n
    

    elif opcao == "s": 
         print("Encerrando o sistema")
         break
        
    else:
         print("Opção em válida")


     