#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

#Recebimento dos dois numeros inteiros

n1= int(input("Insira o primeiro número:"))
n2= int(input("Insira o segundo número:"))

#uso do menor e maior para processar os valores entre eles

menor = min(n1,n2) + 1
maior= max(n1,n2) - 1

#Uso do while para exibir os valores que estão entre eles

while  menor <= maior:
    print(menor)
    menor = menor + 1
