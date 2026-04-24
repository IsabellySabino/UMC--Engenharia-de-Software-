while True:
    try:
        while True:
            pop_a= float(input("\nPopulação de A: "))
            if pop_a> 0: break
            print("A população deve ser maior que zero.")

        while True:
            pop_b= float(input("\nPopulação de B: "))
            if pop_b> 0: break
            print("A população deve ser maior que zero.")
        
        while True:
            taxa_a= float(input("\nTaxa de crescimento de A: "))
            if taxa_a> 0: break
            print("A taxa de crescimento deve ser maior que zero.")

        while True:
            taxa_b= float(input("\nTaxa de crescimento de B: "))
            if taxa_b> 0: break
            print("A população deve ser maior que zero.")

        anos=0
        t_a=taxa_a/100
        t_b=taxa_b/100
        while pop_a<pop_b:
                pop_a += pop_a * t_a
                pop_b += pop_b * t_b
                anos +=1
        print (f"\nSeraõ necessários {anos} anos para que a população de A ultrapasse ou iguale a de B.")
        print(f"\nPopulação A: {pop_a:.0f} habitantes.")
        print(f"\nPopulação B: {pop_b:.0f} habitantes.")
    except ValueError:
         print("Digite apenas números e utilize ponto para decimais.")
    
    não=input("\nDeseja realizar outro cálculo? (s/n): ").lower
    if não !='n':
         break
 


