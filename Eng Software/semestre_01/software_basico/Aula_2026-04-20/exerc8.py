p1 = float(input("Qual o valor do notebook da Samsung? "))
p2 = float(input("Qual o valor do notebook da Apple? "))
p3 = float(input("Qual o valor do notebook da Lenovo? "))

#processamento 
if p1 < p2 and p1 < p3:
    print("O notebook da Samsung é o escolhido e tem o melhor custo benefício")

elif p2 < p1 and p2 < p3:
    print("O notebook da Apple é o escolhido e tem o melhor custo benefício")

elif p3 < p1 and p3 < p2:
    print("O notebook da Lenovo é o escolhido e tem o melhor custo benefício")
# caso todos os produtos sejam do mesmo valor 
else:
    print("Todos tem o mesmo custo benefício")
