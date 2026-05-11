# taxa e custo são parametros 
def soma_imposto(taxa_imposto, custo):
    # dividi o imposto por 100 e depois multipliquei pelo custo para saber o valor do imposto
    imposto = taxa_imposto / 100 * custo
    # adicionei o custo mais o imposto para saber o valor final
    valor = custo + imposto
    # retornei valor para me dar o resultado, sem ele dá erro
    return valor

custo = float(input("Digite o valor do custo: "))
taxa = float(input("Digite o valor da taxa: "))

# aqui eu chamo a função e coloco a taxa como taxa_imposto e custo como custo
resultado = soma_imposto(taxa, custo)

print(f"O valor do imposto é: {resultado} ")