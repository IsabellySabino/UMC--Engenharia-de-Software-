n1= float(input("Insira a primeira nota: "))
n2= float(input("Insira a segunda nota: "))

media = (n1 + n2)/2

if media >= 9: 
    print(f"As notas são {n1} e {n2}\n A média é {media}\nO conceito corresponde é A e foi APROVADO")

elif media >=7.5 :
    print(f"As notas são {n1} e {n2}\n A média é {media}\nO conceito corresponde é B e foi APROVADO")
    
elif media >= 6:
    print(f"As notas são {n1} e {n2}\n A média é {media}\nO conceito corresponde é C e foi APROVADO")

elif media >=4:
    print(f"As notas são {n1} e {n2}\n A média é {media}\nO conceito corresponde é D e foi REPROVADO")

else: 
    print(f"As notas são {n1} e {n2}\n A média é {media}\nO conceito corresponde é E e foi REPROVADO")