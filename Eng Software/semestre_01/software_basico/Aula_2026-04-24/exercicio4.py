
pop_A=80000
taxa_a=0.03 #3%

pop_B=200000
taxa_b=0.015 #1.5%

anos=0

while pop_A < pop_B:
    pop_A += pop_A * taxa_a
    pop_B += pop_B * taxa_b
    anos +=1
print (f"\nSeraõ necessários {anos} anos para que a população de A ultrapasse ou iguale a de B.")
print(f"\nPopulação A: {pop_A:.0f} habitantes.")
print(f"\nPopulação B: {pop_B:.0f} habitantes.")

