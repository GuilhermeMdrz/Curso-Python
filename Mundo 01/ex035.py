print('-=-' * 20)
print('analisador de triângulos...')
print('-=-' * 20)
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a < b + c and b < c + a and c < a + b:
    print('Os segmentos PODEM formar um triângulo.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
