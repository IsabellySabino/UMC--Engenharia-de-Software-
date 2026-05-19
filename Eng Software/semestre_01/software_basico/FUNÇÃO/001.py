def saudacao(nome):
    print(f'Bom dia, {nome}')
    return nome 

nome = input('Qual é o seu nome?').upper()
resultado = saudacao(nome)

print()
print(saudacao)