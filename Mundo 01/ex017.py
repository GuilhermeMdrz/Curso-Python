from math import hypot
c1 = float(input('Digite o valor do primeiro cateto:'))
c2 = float(input('E agora o do segundo cateto:'))
hi = hypot(c1,c2)
print('A hipotenusa desse triângulo retângulo, equivale a {:.2}.'.format(hi))
