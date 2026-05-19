def media(a, b, c):
    media = (n1 + n2 + n3)/3
    print(f'As notas são {n1}, {n2} e {n3}\nA média é {media}')
    return media


n1 = float(input('Digite a primera nota : '))
n2 = float(input('Digite a segunda nota : '))
n3 = float(input('Digite a terceira nota : '))


resultado = media(n1, n2, n3)