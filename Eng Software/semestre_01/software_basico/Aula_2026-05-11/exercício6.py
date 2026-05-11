lista=[]
 
while True:
    print("\n--Menu de compras--")
    print("\n 1) Adicionar item")
    print("\n 2) Remover item")
    print("\n 3) Listar itens")
    print("\n 4) Sair")
 
    opcao= input("Insira a opção: ")
   
    if opcao == '1':
        item=input("Insira o nome do item a ser adcionado a lista: ")
        lista.append(item)
        print(f"{item} foi adicionado a lista de compras.")
   
    elif opcao == '2':
        item=input("Digite o nome do item a ser removido")
        if item in lista:
            lista.remove(item)
            print(f"{item} removido com sucesso.")
       
        else:
            print(f"{item} não encontrado na lista.")
   
 
    elif opcao == '3':
        print("\nSua Lista:")
        if not lista:
            print("\nA lista está vazia.")
       
        else:
            for i, item in enumerate(lista, start=1):
                print(f"{i}.  {item}")
   
    elif opcao == '4':
        print("Lista encerrada!")
        break
 
    else:
        print("Opção inválida. Tente novamente.")