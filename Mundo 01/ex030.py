n = int(input('Digite um número para saber se ele é par ou ímpar:'))
r = n % 2
if r == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))

