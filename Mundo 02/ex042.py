print('-=-' * 20)
print('analisador de triângulos...')
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a < b + c and b < c + a and c < a + b:
    print('Os segmentos PODEM formar um triângulo.')
    if a == b == c:
        print('Esse triângulo classifica-se como EQUILÁTERO.')
    elif a == b or b == c or c == a:
        print('Esse triângulo classifica-se como ISÓSCELES.')
    else:
        print('Esse triângulo classifica-se como ESCALENO.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
print('-=-' * 20)
