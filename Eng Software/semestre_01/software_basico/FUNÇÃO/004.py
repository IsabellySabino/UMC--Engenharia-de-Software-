def temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
    
celsius = int(input('Digite a temperatura em graus Celsius: '))

fahrenheit = temperatura(celsius)


print(f'O grau celsius é {celsius}°C e em fahrenheit é {fahrenheit}°F')