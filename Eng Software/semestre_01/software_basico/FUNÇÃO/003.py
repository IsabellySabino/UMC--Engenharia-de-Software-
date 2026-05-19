def numero(n):
    if n % 2 == 0:
        return True
        
    elif n % 2 == 1:
        return False
      
  
n = int(input('Digite um número: '))

resultado = numero(n)
    
print(resultado)