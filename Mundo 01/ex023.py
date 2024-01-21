número = int(input('Digite um número:'))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print('Ao analisar esse número percebe-se que ele tem...')
print('{} unidades.'.format(u))
print('{} dezenas.'.format(d))
print('{} centenas.'.format(c))
print('E {} milhares.'.format(m))
