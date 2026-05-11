def retangulo(linhas, colunas):
    if linhas < 1 or colunas < 1 :
        altura = 1
        largura = 2

    elif linhas > 20 or colunas > 20:
        altura = 20
        largura = 20

    print("+" + "-" * colunas + "+")

    for i in range (linhas - 2):
        print("|" + " " * colunas + "|")

    print("+" + "-" * colunas + "+")


altura= int(input("Digite a altura do retângulo: "))
largura = int( input("Digite a largura do retângulo: "))
resultado= retangulo(altura, largura)