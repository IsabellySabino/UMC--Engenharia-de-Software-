import itertools

def quadrados():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    
    for p in itertools.permutations(numeros):

    # linhas
        soma1 = p[0] + p[1] + p[2]
        soma2 = p[3] + p[4] + p[5]
        soma3 = p[6] + p[7] + p[8]
        
        # colunas
        soma4 = p[0]+p[3]+p[6]
        soma5 = p[1]+p[4]+p[7]
        soma6 = p[2]+p[5]+p[8]

        # diagonal
        soma7 = p[0]+p[4]+p[8] 
        soma8 = p[6]+p[4]+p[2]

        if soma1 == soma2 == soma3 == soma4 == soma5 == soma6 == soma7 == soma8:
            count += 1
            print(f"Quadrado Mágico {count}:")
            print(f"{p[0]} {p[1]} {p[2]}")
            print(f"{p[3]} {p[4]} {p[5]}")
            print(f"{p[6]} {p[7]} {p[8]}")

quadrados()
    